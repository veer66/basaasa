"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from basaasa.model import meta
from pylons import request, response, session, tmpl_context as c
from basaasa.lib.user import is_admin

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            c.is_admin = is_admin()
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()
