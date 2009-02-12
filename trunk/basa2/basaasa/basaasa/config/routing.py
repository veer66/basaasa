"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    
    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/doc/history/{doc_id}/view/{version}', controller='doc', action='history_view')
    
    map.connect('/trans/edit/{doc_id}', controller='trans', action='edit')
    map.connect('/trans/new/{doc_id}', controller='trans', action='new')
    map.connect('/trans/create/{doc_id}', controller='trans', action='create')
    map.connect('/trans/save/{doc_id}', controller='trans', action='save')
    
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    
    map.connect('/', controller='doc', action='list')

    return map
