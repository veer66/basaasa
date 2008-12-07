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

class NewDocForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    title = formencode.validators.String(not_empty=True)
    body = formencode.validators.String(not_empty=True)

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

class DocController(BaseController):
    @authorize(ValidAuthKitUser())    
    def __before__(self):
        pass
    
    def list(self):
        page = request.params.get('page', 1)
        docs = model.Document.list()
        c.paginator = paginate.Page(docs, page = page)  
        return render("/derived/doc/list.html")

    def new(self):
        return render("/derived/doc/new.html")

    @restrict('POST')
    @validate(schema=NewDocForm(), form='new')    
    def create(self):
        document = model.Document()
        document.title = self.form_result.get('title')
        document.body = self.form_result.get('body')
        document.latest_editor = get_user_model()
        model.meta.Session.flush()        
        redirect_to(action="list")
        
    def view(self, id=None):
        if id is None:
            abort(404)
        c.document = model.Document.get(id)        
        return render("/derived/doc/view.html")
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        values = {"title": document.title, "body": document.body}
        return htmlfill.render(render("/derived/doc/edit.html"), values)
    
    @restrict('POST')
    @validate(schema=NewDocForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(document, k) != v:
                setattr(document, k, v)
        document.latest_editor = get_user_model()
        model.meta.Session.flush()
        redirect_to(action="view", id=id)
        
    def delete(self, id=None):
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        c.document = document
        document.lazy_delete()
        model.meta.Session.flush()
        return render('/derived/doc/deleted.html')
