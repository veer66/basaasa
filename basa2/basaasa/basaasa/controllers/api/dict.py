import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize

from pylons.i18n.translation import _, set_lang

from pylons.decorators import rest, jsonify

from pylons.controllers.util import abort, redirect_to 

from basaasa import model

log = logging.getLogger(__name__)

class DictController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
    
    @rest.dispatch_on(POST="create_entry")
    @rest.dispatch_on(PUT="update_entry")
    @rest.dispatch_on(GET="retrieve_entry")
    @rest.dispatch_on(DELETE="delete_entry")
    def entry(self, id=None):
        return "entry:" + str(id)
    
    def create_entry(self, dict=None, key=None):
        return "create:" + str(key) + ":" + str(dict)
    
    def update_entry(self, dict=None, key=None):
        return "update:" + str(id)
    
    def retrieve_entry(self, dict=None, key=None):
        return "retrieve:" + str(id)
    
    def delete_entry(self, dict=None, key=None):
        return "delete:" + str(key) + ":" + str(dict)

    @rest.dispatch_on(POST="create_dict")
    @rest.dispatch_on(PUT="update_dict")
    @rest.dispatch_on(GET="retrieve_dict")     
    @rest.dispatch_on(DELETE="delete_dict")
    def dict(self):
        pass
    
    def create_dict(self, dict=None):
        if dict == None:
            abort(400)
        if model.Dictionary.query.filter_by(name = dict).count() > 0:
            abort(422)
        else:
            new_dict = model.Dictionary()
            new_dict.name = dict
            model.meta.Session.flush()
    
    def update_dict(self, dict=None):
        if dict == None:
            abort(400)
        name = request.params["name"]
        dicts = model.Dictionary.query.filter_by(name = dict).all()            
        if len(dicts) != 1:
            abort(422)
        else:            
            dicts[0].name = name
            model.meta.Session.flush()
            
    @jsonify
    def retrieve_dict(self, dict=None):
        if dict != None:
            dicts = model.Dictionary.query.filter_by(name = dict).all()
            if len(dicts) != 1:
                abort(442)
            else:
                dict0 = dicts[0]
                return {"id": dict0.id, "name": dict0.name}
        else:
            dicts = model.Dictionary.query.all()
            return [{"id": d.id, "name":d.name} for d in dicts]
        
    def delete_dict(self, dict=None):
        if dict == None:
            abort(400)
        dicts = model.Dictionary.query.filter_by(name = dict).all()
        if len(dicts) != 1:
            abort(442)
        else:
            model.meta.Session.delete(dicts[0])
            model.meta.Session.flush()
