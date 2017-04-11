# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='render_attachment')
def render_attachment(data):
    """Render attachment."""
    
    if data.get('content_type', '').startswith('image'):
        string = '<a href="{url}"><img src="{url}"></a>'
    else:
        string = '<a href="{url}">{name}</a>'

    return mark_safe(string.format(**data))