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

class NewDocForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    title = formencode.validators.String(not_empty=True)
    body = formencode.validators.String(not_empty=True)

class DocController(BaseController):
    @authorize(RemoteUser())    
    def __before__(self):
        pass
    
    def list(self):
        page = request.params.get('page', 1)
        docs = model.Document.list()
        c.paginator = paginate.Page(docs, page = page)  
        return render("/derived/doc/list.html")

    def new(self):
        return render("/derived/doc/new.html")

    def tm(self, id):
        fragment = request.params.get('fragment', 1)
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        ans = document.get_similar_fragments(fragment)
        return simplejson.dumps(ans)
    
    @restrict('POST')
    @validate(schema=NewDocForm(), form='new')    
    def create(self):
        document = model.Document()
        document.title = self.form_result.get('title')
        document.body = self.form_result.get('body')
        document.latest_editor = get_user()
        model.meta.Session.flush()        
        redirect_to(controller="segment",action="edit",id=document.id)
        
    def view(self, id=None):
        if id is None:
            abort(404)
        c.document = model.Document.get(id) 
        c.translation = c.document.latest_translation()       
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
        document.latest_editor = get_user()
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
    
    def history(self, id=None):
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        versions = document.versions[:-1]
        versions.reverse()
        page = request.params.get('page', 1)
        docs = model.Document.list()
        c.paginator = paginate.Page(versions, page = page)  
        return render('/derived/doc/history.html')

    def history_view(self, doc_id=None, version=None):
        if doc_id is None or version is None:
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)
        c.translations = document.translations[0].versions  
        c.version = document.get_version_with_editor(version)
        return render('/derived/doc/history_view.html')        
