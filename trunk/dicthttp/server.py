from wsgiref.simple_server import make_server, demo_app
from dicthttp import dicthttp_app

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(dicthttp_app, host='127.0.0.1', port='8000')