import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize
from webhelpers import paginate  

from pylons.decorators import validate
from pylons.decorators.rest import restrict

import formencode
from formencode import htmlfill

from basaasa import model

log = logging.getLogger(__name__)

def get_user():
    return request.environ['authkit.users'].user(request.environ['REMOTE_USER'])

def get_user_id():
    username = get_user().get('username')
    user = model.User.query.filter_by(username=username).one()
    return user.uid

def get_user_model():
    username = get_user().get('username')
    user = model.User.query.filter_by(username=username).one()
    return user

class NewTransForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    title = formencode.validators.String(not_empty=True)
    body = formencode.validators.String(not_empty=True)

# This implementation is for bitext only 
# TODO: multilingual

class TransController(BaseController):
    @authorize(ValidAuthKitUser())    
    def __before__(self):
        pass

    def index(self):
        return "trans"
    
    def edit(self, doc_id=None):
        if doc_id is None:  
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)
        c.document = document
        if not document.is_exist_translation():
            redirect_to(action="new", doc_id=doc_id)
        else: 
            translation = document.latest_translation()    
            values = {"title": translation.title,  
                      "body": translation.body}
            return htmlfill.render(render("/derived/trans/edit.html"), values)

    def new(self, doc_id=None):
        if doc_id is None:  
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)
        c.textunits = document.textunits()
        return render("/derived/trans/new.html")
    
    @restrict('POST')
    @validate(schema=NewTransForm(), form='new')
    def create(self, doc_id):
        if doc_id is None:  
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)
        translation = model.Translation(document = document,
                                       title = self.form_result.get('title'),
                                       body = self.form_result.get('body'),
                                       latest_editor = get_user_model())
        model.meta.Session.flush()
        redirect_to(controller="doc", action="view", id=doc_id)
    
    @restrict('POST')
    @validate(schema=NewTransForm(), form='edit')
    def save(self, doc_id=None):
        if doc_id is None:
            abort(404)
        document = model.Document.get(doc_id)        
        if document is None:
            abort(404)
        translation = document.latest_translation()
        for k, v in self.form_result.items():
            if getattr(translation, k) != v:
                setattr(translation, k, v)
        translation.latest_editor = get_user_model()
        model.meta.Session.flush()
        redirect_to(controller="doc", action="view", id=doc_id)
