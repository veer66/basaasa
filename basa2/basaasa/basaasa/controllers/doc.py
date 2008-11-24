import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize
from webhelpers import paginate  

from basaasa import model

log = logging.getLogger(__name__)

class DocController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
    
    def list(self):
        page = request.params.get('page', 1)
        documents = model.Document.query.all()
        c.paginator = paginate.Page(documents, page = page)  
        return render("/derived/doc/list.html")
    
    