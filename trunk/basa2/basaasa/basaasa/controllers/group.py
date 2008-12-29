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

class NewGroupForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)
    
class GroupController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
    
    def list(self):
        page = request.params.get('page', 1)
        groups = model.Group.query.all()
        c.paginator = paginate.Page(groups, page = page)  
        return render("/derived/group/list.html")
    
    def new(self):
        return render("/derived/group/new.html")

    @restrict('POST')
    @validate(schema=NewGroupForm(), form='new')    
    def create(self):
        group = model.Group()
        for k, v in self.form_result.items():
            setattr(group, k, v)        
        model.meta.Session.flush()
        redirect_to(action="list")
        
    def view(self, id=None):
        if id is None:
            abort(404)
        c.group = model.Group.get(id)        
        return render("/derived/group/view.html")
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        group = model.Group.get(id)
        if group is None:
            abort(404)
        values = {"name": group.name}
        return htmlfill.render(render("/derived/group/edit.html"), values)
    
    @restrict('POST')
    @validate(schema=NewGroupForm(), form='edit')
    def save(self, id=None):
        if id is None:
            abort(404)
        group = model.Group.get(id)
        if group is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(group, k) != v:
                setattr(group, k, v)
        model.meta.Session.flush()
        redirect_to(action="view", id=id)