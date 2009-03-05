from authkit.authorize import NotAuthenticatedError  
import urlparse
from authkit.permissions import RequestPermission  
from pylons import config

class Admin(RequestPermission):  
     def __init__(self):  
        key = 'basaasa.admins'
        if key not in config:  
            raise RuntimeError, "Require %s" % key  
        self.users = config.get(key).split()  
   
     def check(self, app, environ, start_response):  
        if 'REMOTE_USER' not in environ:  
            raise NotAuthenticatedError('Not Authenticated')  
        if urlparse.urldefrag(environ['REMOTE_USER'])[0] not in self.users:  
            raise NotAuthenticatedError('Not Authenticated')  
        return app(environ, start_response)
