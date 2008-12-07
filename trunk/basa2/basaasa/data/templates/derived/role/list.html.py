from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1228557885.8796589
_template_filename='/home/veer/eclipse4_workspace/basaasa/basaasa/templates/derived/role/list.html'
_template_uri='/derived/role/list.html'
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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n<p>\n<ul>\n<table class="data">\n\t<tr>\n\t\t<td>')
        # SOURCE LINE 12
        __M_writer(escape(_("id")))
        __M_writer(u'</td>\n\t\t<td>')
        # SOURCE LINE 13
        __M_writer(escape(_("name")))
        __M_writer(u'</td>\n\t</tr>\n')
        # SOURCE LINE 15
        for role in c.paginator:
            # SOURCE LINE 16
            __M_writer(u'\t<tr>  \n\t\t<td>')
            # SOURCE LINE 17
            __M_writer(escape(role.uid))
            __M_writer(u'</td> \n\t\t<td>')
            # SOURCE LINE 18
            __M_writer(escape(h.link_to(role.name, h.url_for(action="view", id=role.uid))))
            __M_writer(u'</td>\n\t</tr>\t\t \n')
        # SOURCE LINE 21
        __M_writer(u'<table>\n<p>')
        # SOURCE LINE 22
        __M_writer(escape( c.paginator.pager('~2~') ))
        __M_writer(u'</p>\n</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<div id="header">')
        __M_writer(escape(_(u"Role")))
        __M_writer(u': ')
        __M_writer(escape(_(u"list")))
        __M_writer(u'</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<div id="menu">\n')
        # SOURCE LINE 5
        __M_writer(escape(h.link_to(_(u"New role"), h.url_for(action="new", id=None))))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


