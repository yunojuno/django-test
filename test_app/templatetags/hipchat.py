from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='render_attachment')
def render_attachment(attach_data):
    """render attachment with appropriate html"""
    content_type = attach_data.get('content_type', '')

    if content_type.split('/')[0].lower() == 'image':
        attach_string = '<a href="{url}"><img src="{url}"></a>'
    else:
        attach_string = '<a href="{url}">{name}</a>'

    return mark_safe(attach_string.format(**attach_data))
