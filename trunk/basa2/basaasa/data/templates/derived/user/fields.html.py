from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1228619075.7296979
_template_filename='/home/veer/eclipse4_workspace/basaasa/basaasa/templates/derived/user/fields.html'
_template_uri='/derived/user/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(_(u"Username"), h.text(name="username"), required=True)))
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(escape(h.field(_(u"Password"), h.password(name="password"), required=True)))
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(escape(h.field(_(u"Group"), h.select(name="group_uid", selected_values=[], options=c.groups))))
        return ''
    finally:
        context.caller_stack._pop_frame()


