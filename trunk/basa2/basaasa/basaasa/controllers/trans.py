import logging
from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from basaasa.lib.base import BaseController, render
from authkit.permissions import ValidAuthKitUser
from authkit.authorize.pylons_adaptors import authorize
from webhelpers import paginate  
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import formencode
from formencode import htmlfill
from basaasa import model
import re

log = logging.getLogger(__name__)

def get_user():
    return request.environ['authkit.users'].user(request.environ['REMOTE_USER'])

def get_user_id():
    username = get_user().get('username')
    user = model.User.query.filter_by(username=username).one()
    return user.uid

def get_user_model():
    username = get_user().get('username')
    user = model.User.query.filter_by(username=username).one()
    return user

class NewTransForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = False
    title = formencode.validators.String(not_empty=True)
    body = formencode.validators.String(not_empty=True)

# This implementation is for bitext only 
# TODO: multilingual

class TransController(BaseController):
    @authorize(ValidAuthKitUser())    
    def __before__(self):
        pass

    def index(self):
        return render("/derived/trans/index.html")
        
    def edit(self, doc_id=None):
        if doc_id is None:  
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)
        c.document = document
        if not document.is_exist_translation():
            redirect_to(action="new", doc_id=doc_id)
        else: 
            translation = document.latest_translation() 
        pairs = zip(document.segment, translation.body)
        c.title = translation.title
        c.body = pairs
        c.source_title = document.title
        c.use_google = True
        return render("/derived/trans/edit.html")

    def new(self, doc_id=None):
        if doc_id is None:  
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)
        c.document = document
        c.source_title = document.title
        c.title = ""
        c.body = zip(document.segment, ["" for i in range(len(document.segment))])
        c.use_google = True
        return render("/derived/trans/new.html")

    def create(self, doc_id):
        if doc_id is None:  
            abort(404)
        document = model.Document.get(doc_id)
        if document is None:
            abort(404)

        target_items = [(int(re.match("^target_(\d+)$", i[0]).group(1)), i[1]) \
                        for i in request.params.items() if \
                            re.match("^target_\d+$", i[0])]
        target_items.sort(lambda a, b: cmp(a[0], b[0]))
        target_segments = [i[1] for i in target_items]

        translation = model.Translation(document = document,
                                       title = request.params.get('title'),
                                       body = target_segments,
                                       latest_editor = get_user_model())
        model.meta.Session.flush()
        redirect_to(controller="doc", action="view", id=doc_id)
    
    def save(self, doc_id=None):
        if doc_id is None:
            abort(404)
        document = model.Document.get(doc_id)        
        if document is None:
            abort(404)
        translation = document.latest_translation()
        translation.latest_editor = get_user_model()
        translation.title = request.params.get('title')
        target_items = [(int(re.match("^target_(\d+)$", i[0]).group(1)), i[1]) \
                        for i in request.params.items() if \
                            re.match("^target_\d+$", i[0])]
        target_items.sort(lambda a, b: cmp(a[0], b[0]))
        target_segments = [i[1] for i in target_items]
        translation.body = target_segments
        model.meta.Session.flush()
        redirect_to(controller="doc", action="view", id=doc_id)
