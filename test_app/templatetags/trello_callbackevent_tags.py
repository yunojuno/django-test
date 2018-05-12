# template tags used in HipChat event template
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def attachment_name_or_inline_image(attachment):
    """
    Returns attachment name text or safe inline 'img' node with attachment url
    as source.
    """
    name = attachment['name']
    content_type = attachment.get('content_type', '')

    # render safe html 'img' tag only if content_type is image
    if content_type.startswith('image/'):
        tmpl = u'<img src="%s" alt="%s">' % (attachment['url'], name)
        return mark_safe(tmpl)

    return name
