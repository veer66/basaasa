import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from basaasa.lib.base import BaseController, render

from authkit.authorize.pylons_adaptors import authorize

from pylons.i18n.translation import _, set_lang

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def signout(self):
        return 'signout'
