from pylons import request
from pylons import config
import urlparse

def get_user():
    return request.environ.get('REMOTE_USER')

def has_remote_user():
    return 'REMOTE_USER' in request.environ    
    
def is_admin():
    key = 'basaasa.admins'
    if key not in config:  
        raise RuntimeError, "Require %s" % key  
    users = config.get(key).split()  
    return ('REMOTE_USER' in request.environ) and \
           urlparse.urldefrag(request.environ['REMOTE_USER'])[0] in users
