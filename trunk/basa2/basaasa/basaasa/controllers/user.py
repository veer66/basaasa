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

class NewUserForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    username = formencode.validators.String(not_empty=True)
    password = formencode.validators.String(not_empty=True)
    group_uid = formencode.validators.Int()

class UserController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
    
    def list(self):
        page = request.params.get('page', 1)
        users = model.User.query.all()
        c.paginator = paginate.Page(users, page = page)  
        return render("/derived/user/list.html")
    
    def new(self):
        c.groups = [(g.uid, g.name) for g in model.Group.query.all()]
#        c.groups = ["foo", "titi"]
        return render("/derived/user/new.html")

    @restrict('POST')
    @validate(schema=NewUserForm(), form='new')    
    def create(self):
        user = model.User(self.form_result['username'])
        for k, v in self.form_result.items():
            if k != 'username':
                setattr(user, k, v)        
        model.meta.Session.flush()
        redirect_to(action="list")
        
    def view(self, id=None):
        if id is None:
            abort(404)
        c.user = model.User.get(id)        
        return render("/derived/user/view.html")
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        user = model.User.get(id)
        if user is None:
            abort(404)
        values = {"username": user.username}
        c.groups = model.Group.query.all()
        return htmlfill.render(render("/derived/user/edit.html"), values)
    
    @restrict('POST')
    @validate(schema=NewUserForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        user = model.User.get(id)
        if user is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(user, k) != v:
                setattr(user, k, v)
        model.meta.Session.flush()
        redirect_to(action="view", id=id)
        
    def delete(self, id=None):
        if id is None:
            abort(404)
        user = model.User.get(id)
        if user is None:
            abort(404)
        c.user = user
        model.meta.Session.delete(user)
        model.meta.Session.flush()
        return render('/derived/user/deleted.html')
