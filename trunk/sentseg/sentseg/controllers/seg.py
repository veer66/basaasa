import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from sentseg.lib.base import BaseController, render
#from sentseg import model

log = logging.getLogger(__name__)

from pylons.decorators import jsonify
from nltk.tokenize.punkt import PunktSentenceTokenizer as Tokenizer


class SegController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'

    @jsonify
    def segment(self):
        text = request.params.get('text')
        lang = request.params.get('lang', 'eng')
        tokenizer = Tokenizer()
        toks = tokenizer.tokenize(text)
        return toks
