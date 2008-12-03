import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from dicthttp.lib.base import BaseController, render
#from dicthttp import model

log = logging.getLogger(__name__)

class DictController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
