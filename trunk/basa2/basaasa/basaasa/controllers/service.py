import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.authorize.pylons_adaptors import authorize

from pylons.decorators import validate
from pylons.decorators.rest import restrict
from basaasa.lib.permissions import Admin
from basaasa import model
import re

import urllib

from routes import url_for

import simplejson
from webhelpers import paginate

import formencode
from formencode import htmlfill

log = logging.getLogger(__name__)

class NewServiceForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)
    type = formencode.validators.String(not_empty=True)
    url = formencode.validators.URL(add_http=True)


class ServiceController(BaseController):
    def __before__(self):
        pass

    @authorize(Admin())    
    def list(self):
        page = request.params.get('page', 1)
        service = model.Service.query.all()
        c.paginator = paginate.Page(service, page = page)  
        return render("/derived/service/list.html")

    @authorize(Admin())    
    def new(self):
        return render("/derived/service/new.html")

    @authorize(Admin())    
    @restrict('POST')
    @validate(schema=NewServiceForm(), form='new')    
    def create(self):
        service = model.Service()
        service.name = self.form_result.get('name')
        service.type = self.form_result.get('type')
        service.url = self.form_result.get('url')
        model.meta.Session.flush()        
        redirect_to(controller="service", action="list")
        
    @authorize(Admin())    
    def view(self, id=None):
        if id is None:
            abort(404)
        c.service = model.Service.get(id)                
        return render("/derived/service/view.html")
    
    @authorize(Admin())    
    def delete(self, id=None):
        if id is None:
            abort(404)
        service = model.Service.get(id)
        if service is None:
            abort(404)
        model.meta.Session.delete(service)
        model.meta.Session.flush()
        return render('/derived/service/deleted.html')
    
    def dict(self):
        word = request.params.get("word")
        if word is None:
            abort(404)
        service = model.Service.query.filter_by(type='dict').first()
        if service is None:
            abort(404)
        url = service.url
        return urllib.urlopen(url + "/d:" + urllib.quote_plus(word.encode("UTF-8"))).read()
    
    def transliterate(self):
        input = request.params.get("input")
        if input is None:
            abort(404)
        service = model.Service.query.filter_by(type='transliterate').first()
        if service is None:
            abort(404)    
        url = service.url
        return urllib.urlopen(url, urllib.urlencode(dict(input=input))).read()

    def translate(self):
        service = model.Service.query.filter_by(type='translate').first()
        if service is None:
            abort(404)
        url = service.url
        def trans(source):
            return urllib.urlopen(url, urllib.urlencode(dict(source=source, format='text'))).read()
        source = request.params.get("source")
        if source is None:
            abort(404)
        return simplejson.dumps(map(trans, simplejson.loads(source)))
    
    def segment(self):
        service = model.Service.query.filter_by(type='segment').first()
        if service is None:
            abort(404)
        url = service.url        
        text = request.params.get("text")
        lang = request.params.get("lang")
        if lang is None or lang is None:
            abort(404)
        return urllib.urlopen(url, urllib.urlencode(dict(text=text, lang=lang))).read()
    
    @authorize(Admin())    
    def edit(self, id=None):
        if id is None:
            abort(404)
        service = model.Service.get(id)
        if service is None:
            abort(404)
        values = dict(name = service.name, \
                      type = service.type, \
                      url = service.url)        
        return htmlfill.render(render("/derived/service/edit.html"), values)
    
    @authorize(Admin())    
    @restrict('POST')
    @validate(schema=NewServiceForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        service = model.Service.get(id)
        if service is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(service, k) != v:
                setattr(service, k, v)
        model.meta.Session.flush()
        redirect_to(action="view", id=id)
