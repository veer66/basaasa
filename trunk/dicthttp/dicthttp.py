import re
from dict_client_wrapper import DictClientWrapper, DictClientError
from simplejson import dumps

class PathError(RuntimeError):
    pass

DEFINE_PAT = re.compile("^\/d:(.+)")
MATCH_PAT = re.compile("^\/m:(.+)")
COLON = re.compile(":")
class DictHttp:
    def __init__(self):
        self.wrapper = DictClientWrapper("dict.org")

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
        json_result = dumps(result)
        return json_result

    def define(self, raw_params):
        params = COLON.split(raw_params)
        ans = self.create_attr_val(["word", "database", "n"], params)
        result = self.wrapper.define(*params)
        json_result = dumps(result)
        return json_result

    def close(self):
        self.wrapper.close()

def dicthttp_app(environ, start_response):
    try:
        dicthttp = DictHttp()
        path = environ['PATH_INFO']
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


