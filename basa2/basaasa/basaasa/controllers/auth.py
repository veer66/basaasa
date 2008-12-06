import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize

from pylons.i18n.translation import _, set_lang

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'
    
    def tmpl(self):
        session['flash'] = _(u"flash")
        session.save()
        return render("/derived/auth/index.html")
    
    @authorize(ValidAuthKitUser())    
    def private(self):
        return 'private'
    
    def signout(self):
        return 'signout'