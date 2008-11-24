from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1227530940.15131
_template_filename='/home/veer/eclipse4_workspace/basaasa/basaasa/templates/derived/role/new.html'
_template_uri='/derived/role/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace('fields', context._clean_inheritance_tokens(), templateuri='fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'fields')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        fields = _mako_get_namespace(context, 'fields')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n<p>\n')
        # SOURCE LINE 5
        __M_writer(escape(h.form_start(h.url_for(controller='role', action='create'), method="post")))
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(escape(fields.body()))
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(escape(h.field(field=h.submit(value=_(u"Create Role"), name='submit'))))
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n</p>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'<div id="header">')
        __M_writer(escape(_(u"Role")))
        __M_writer(u': ')
        __M_writer(escape(_(u"new")))
        __M_writer(u'</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


