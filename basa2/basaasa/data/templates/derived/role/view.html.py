from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1228562742.2056479
_template_filename='/home/veer/eclipse4_workspace/basaasa/basaasa/templates/derived/role/view.html'
_template_uri='/derived/role/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header', 'menu']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n<p>\n')
        # SOURCE LINE 10
        __M_writer(escape(c.role.uid))
        __M_writer(u':\n')
        # SOURCE LINE 11
        __M_writer(escape(c.role.name))
        __M_writer(u'\n</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<div id="header">')
        __M_writer(escape(_(u"Role")))
        __M_writer(u': ')
        __M_writer(escape(_(u"view")))
        __M_writer(u' ')
        __M_writer(escape(c.role.uid))
        __M_writer(u'</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<div id="menu">\n')
        # SOURCE LINE 5
        __M_writer(escape(h.link_to(_(u"Edit"), h.url_for(action="edit", id=c.role.uid))))
        __M_writer(u' |\n')
        # SOURCE LINE 6
        __M_writer(escape(h.link_to(_(u"List roles"), h.url_for(action="list", id=None))))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


