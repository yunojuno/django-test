# # -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_attachment_link(attachment):
    """Render attachment link based on content type."""
    if 'content_type' in attachment:
        if attachment['content_type'].startswith("image/"):
            # Render link with image
            html = '<a href="{0}"><img src={0}></a>'.format(
                attachment.get('url'))
            return mark_safe(html)
    # Render link with name
    html = '<a href="{}">{}</a>'.format(
        attachment.get('url'),
        attachment.get('name'))
    return mark_safe(html)
