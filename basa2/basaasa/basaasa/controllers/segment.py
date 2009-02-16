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

import re

log = logging.getLogger(__name__)

class NewSegmentForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    title = formencode.validators.String(not_empty=True)
    segment = formencode.validators.String(not_empty=True)
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

class SegmentController(BaseController):
    @authorize(ValidAuthKitUser())    
    def __before__(self):
        pass
            
    @restrict('POST')
    @validate(schema=NewSegmentForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        document.title = self.form_result.get('title')
        document.body = self.form_result.get('body')
        document.segment = filter(lambda line: line != '', \
                                  re.split("\n\n+", \
                                           self.form_result.get('segment').replace("\r", "")))
        document.latest_editor = get_user_model()
        model.meta.Session.flush()
        redirect_to(action="view", id=id)       
            
    def edit(self, id=None):
        if id is None:
            abort(404)
        document = model.Document.get(id)
        if document is None:
            abort(404)
        segment = document.segment
        if segment is None:
            segment = ""
        else:
            segment = "\n\n".join(segment) 
        values = {"title": document.title, 
                  "body": document.body, 
                  "segment": segment}
        return htmlfill.render(render("/derived/segment/edit.html"), values)
    
    def view(self, id=None):
        if id is None:
            abort(404)
        c.document = model.Document.get(id) 
        c.translation = c.document.latest_translation()       
        return render("/derived/segment/view.html")
