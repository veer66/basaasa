import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import RemoteUser
from authkit.authorize.pylons_adaptors import authorize
from webhelpers import paginate  

from pylons.decorators import validate
from pylons.decorators.rest import restrict

import formencode
from formencode import htmlfill

from basaasa import model
import simplejson

from basaasa.lib.user import get_user

log = logging.getLogger(__name__)

class NewUserDictForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    headword = formencode.validators.String(not_empty=True)
    lang = formencode.validators.String(not_empty=True)
    translations = formencode.validators.String(not_empty=True)

class UserDictController(BaseController):
    @authorize(RemoteUser())    
    def __before__(self):
        pass
    
    def list(self):
        page = request.params.get('page', 1)
        dict_entries = model.UserDict.query.all()
        c.paginator = paginate.Page(dict_entries, page = page)  
        return render("/derived/user_dict/list.html")

    def new(self):
        return render("/derived/user_dict/new.html")
    
    @restrict('POST')
    @validate(schema=NewUserDictForm(), form='new')    
    def create(self):
        user_dict = model.UserDict()
        user_dict.owner = get_user() 
        user_dict.headword = self.form_result.get('headword')
        user_dict.lang = self.form_result.get('lang')
        user_dict.translations(self.form_result.get('translations').split(", *"))
        model.meta.Session.flush()        
        redirect_to(action="list")
        
    def view(self, id=None):
        if id is None:
            abort(404)
        c.dict_entry = model.UserDict.get(id)        
        return render("/derived/user_dict/view.html")
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        dict_entry = model.UserDict.get(id)
        if dict_entry is None:
            abort(404)            
        
        values = dict(headword=dict_entry.headword,
                      lang=dict_entry.lang,
                      translations=','.join(dict_entry.translations())) 
        return htmlfill.render(render("/derived/user_dict/edit.html"), values)
    
    @restrict('POST')
    @validate(schema=NewUserDictForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        dict_entry = model.UserDict.get(id)
        if dict_entry is None:
            abort(404)
        dict_entry.owner = get_user()
        dict_entry.headword = self.form_result.get('headword')
        dict_entry.lang = self.form_result.get('lang')
        dict_entry.translations(self.form_result.get('translations').split(", *"))
        
        model.meta.Session.flush()
        redirect_to(action="view", id=id)
        
    def delete(self, id=None):
        if id is None:
            abort(404)
        dict_entry = model.UserDict.get(id)
        if dict_entry is None:
            abort(404)
        model.meta.Session.delete(dict_entry)
        model.meta.Session.flush()
        return render('/derived/user_dict/deleted.html')
