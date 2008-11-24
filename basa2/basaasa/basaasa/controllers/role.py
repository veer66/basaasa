import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize
from webhelpers import paginate  

from basaasa import model

from pylons.decorators import validate
from pylons.decorators.rest import restrict

from pylons.controllers.util import abort, redirect_to  

log = logging.getLogger(__name__)

import formencode
from formencode import htmlfill

class NewRoleForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)
    
class RoleController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
    
    def list(self):
        page = request.params.get('page', 1)
        roles = model.Role.query.all()
        c.paginator = paginate.Page(roles, page = page)  
        return render("/derived/role/list.html")
    
    def new(self):
        return render("/derived/role/new.html")

    @restrict('POST')
    @validate(schema=NewRoleForm(), form='new')    
    def create(self):
        role = model.Role()
        for k, v in self.form_result.items():
            setattr(role, k, v)        
        model.meta.Session.flush()
        redirect_to(action="list")
        
    def view(self, id=None):
        if id is None:
            abort(404)
        c.role = model.Role.get(id)        
        return render("/derived/role/view.html")
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        role = model.Role.get(id)
        if role is None:
            abort(404)
        values = {"name": role.name}
        return htmlfill.render(render("/derived/role/edit.html"), values)
    
    @restrict('POST')
    @validate(schema=NewRoleForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        role = model.Role.get(id)
        if role is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(role, k) != v:
                setattr(role, k, v)
        model.meta.Session.flush()
        redirect_to(action="view", id=id)