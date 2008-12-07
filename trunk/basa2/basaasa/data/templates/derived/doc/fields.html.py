from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1228587899.780189
_template_filename='/home/veer/eclipse4_workspace/basaasa/basaasa/templates/derived/doc/fields.html'
_template_uri='/derived/doc/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(_(u"Title"), h.text(name='title'), required=True)))
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(escape(h.field(_(u"Body"), h.textarea(name='body', rows=20, cols=70), required=True)))
        return ''
    finally:
        context.caller_stack._pop_frame()


