import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='render_attachment')
def render_attachment(attachment_data):
    """render attachment with appropriate html"""
    content_type = attachment_data.get('content_type', '')

    if re.match('video/*', content_type):
        attachment_string = '<video src="{url}" controls></video>'
    else:
        attachment_string = '<a href="{url}">{name}</a>'

    return mark_safe(attachment_string.format(**attachment_data))
