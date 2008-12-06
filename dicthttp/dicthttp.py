import re
from dict_client_wrapper import DictClientWrapper, DictClientError
from simplejson import dumps
from paste.request import parse_querystring
from Cheetah.Template import Template
from xml.sax.saxutils import escape

class PathError(RuntimeError):
    pass

DEFINE_PAT = re.compile("^\/d:(.+)")
MATCH_PAT = re.compile("^\/m:(.+)")
COLON = re.compile(":")
class DictHttp:
    def __init__(self, host, format='json'):
        self.wrapper = DictClientWrapper(host)
        self.format = format

    def create_attr_val(self, attrs, vals):
        if len(vals) > len(attrs):
            raise PathError("path contains too many parameters")
        attr_val = {}
        for attr in attrs:
            attr_val[attr] = None
        for i, val in enumerate(vals):
            attr_val[attrs[i]] = val
        return attr_val

    def match(self, raw_params):
        params = COLON.split(raw_params)
        ans = self.create_attr_val(["word", "database", "strat", "n"], params)
        result = self.wrapper.match(*params)
        return self.transform_result(result)

    def define(self, raw_params):
        params = COLON.split(raw_params)
        ans = self.create_attr_val(["word", "database", "n"], params)
        result = self.wrapper.define(*params)
        return self.transform_result(result)

    def transform_result(self, result):
        if self.format == 'xml':
            result = [{'word': escape(entry['word']),
                       'def': escape(entry['def']),
                       'database': escape(entry['database'])} \
                       for entry in result]
            f = open("dictresult.xml")
            t = Template(file=f)
            t.result = result
            transformed_result = str(t)
            f.close()
        else:
            transformed_result = dumps(result)
            
        return transformed_result

    def close(self):
        self.wrapper.close()

def is_valid_hostname(host):
    return (re.match("^[A-Za-z0-9\-\.]+$", host) != None)

def get_params(environ):
    params = {}
    for k, v in parse_querystring(environ):
        params[k] = v

    host = "localhost"
    format = "json"

    if params.has_key('host'):
        if is_valid_hostname(params['host']):
            host = params['host']
    
    if params.has_key('format'):
        if params['format'] == 'xml':
            format = params['format']

    return host, format

def dicthttp_app(environ, start_response):
    try:
        path = environ['PATH_INFO']
        host, format = get_params(environ)

        dicthttp = DictHttp(host, format)

        if path is None or path == "":
            raise PathError("path is empty")

        result = None
        m = DEFINE_PAT.match(path)
        if m:
            result = dicthttp.define(m.group(1))
        else:
            m = MATCH_PAT.match(path)
            if m:
                result = dicthttp.match(m.group(1))
            else:
                raise PathError("path is not match with any command")

        if format == 'xml':
            start_response('200 OK', [
                           ('Content-Type', 'text/xml')])
        else:
            start_response('200 OK', [
                           ('Content-Type', 'application/json')])
        dicthttp.close()
        return result
    except PathError, e:
        start_response('500 INTERNAL SERVER ERROR', [
                       ('Content-Type', 'text/plain')])
        return str(e)
    except DictClientError, e:
        start_response('500 INTERNAL SERVER ERROR', [
                       ('Content-Type', 'text/plain')])
        return str(e)


