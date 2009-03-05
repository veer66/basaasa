import logging
log = logging.getLogger(__name__)
class foomid(object): 
    def __init__(self, app, app_conf):
        self.app = app

    def __call__(self, environ, start_response):
        a = [str(e) for e in environ]
        a.sort()
        log.info("\n".join(a))
        response = self.app(environ, start_response)
        return response
