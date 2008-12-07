from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1228619215.8869641
_template_filename='/home/veer/eclipse4_workspace/basaasa/basaasa/templates/base/index.html'
_template_uri='/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'maintab', 'title', 'menu', 'flash', 'header']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n"http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n    <title>')
        # SOURCE LINE 7
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 8
        __M_writer(escape(self.head()))
        __M_writer(u'\n</head>\n<body>\n\t')
        # SOURCE LINE 11
        __M_writer(escape(self.maintab()))
        __M_writer(u'\n\t')
        # SOURCE LINE 12
        __M_writer(escape(self.header()))
        __M_writer(u'\n\t\n\t')
        # SOURCE LINE 14
        __M_writer(escape(self.flash()))
        __M_writer(u'\n    ')
        # SOURCE LINE 15
        __M_writer(escape(next.body()))
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(escape(self.menu()))
        __M_writer(u'\n</body>\n</html>\n')
        # SOURCE LINE 19
        __M_writer(u'\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/main.css'))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_maintab(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n<div id="maintab">')
        # SOURCE LINE 21
        __M_writer(escape(h.link_to(label=_(u"Home"), url=h.url_for(controller="doc", action="list"))))
        __M_writer(u' | \n')
        # SOURCE LINE 22
        __M_writer(escape(h.link_to(label=_(u"Logout"), url=h.url_for(controller="auth", action="signout", id=None))))
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(escape(_(u"BasaAsa")))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flash(context):
    context.caller_stack._push_frame()
    try:
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        if session.has_key('flash'):
            # SOURCE LINE 29
            __M_writer(u'    <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\n    ')
            # SOURCE LINE 30
  
            del session['flash']
            session.save()
                
            
            # SOURCE LINE 33
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'<div id="header">')
        __M_writer(escape(_(u"base")))
        __M_writer(u'</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


