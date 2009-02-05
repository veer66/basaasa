import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize

from pylons.decorators import validate
from pylons.decorators.rest import restrict

from basaasa import model
import re

import urllib

from routes import url_for

log = logging.getLogger(__name__)

import simplejson

class ServiceController(BaseController):
    def index(self):
        pass
    
    def dict(self):
        word = request.params.get("word")
        if word is None:
            abort(404)
        url = "http://vivaldi.cpe.ku.ac.th/~vee/wsgi-scripts/dict.wsgi/d:"
        return urllib.urlopen(url + urllib.quote_plus(word.encode("UTF-8"))).read()
    
    def transliterate(self):
        input = request.params.get("input")
        if input is None:
            abort(404)
        url = "http://vivaldi.cpe.ku.ac.th/~vee/tubsube2t"
        return urllib.urlopen(url, urllib.urlencode(dict(input=input))).read()

    def translate(self):
        url = "http://vivaldi.cpe.ku.ac.th/mt"
        def trans(source):
            return urllib.urlopen(url, urllib.urlencode(dict(source=source, format='text'))).read()
        source = request.params.get("source")
        if source is None:
            abort(404)
        return simplejson.dumps(map(trans, simplejson.loads(source)))
    
    def segment(self):
        url = "http://vivaldi.cpe.ku.ac.th/~vee/segment.php";
        text = request.params.get("text")
        lang = request.params.get("lang")
        if lang is None or lang is None:
            abort(404)
        return urllib.urlopen(url, urllib.urlencode(dict(text=text, lang=lang))).read()