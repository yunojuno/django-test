# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_attachment(attachment_data):
    """
    Render attachment to correct html.
    If attachment data has an image type, template will be formatted with img tag.
    Otherwise if will be formatted as a simple url
    """
    content_type = attachment_data.get('content_type', '')
    attachment_is_image = content_type.split('/')[0].lower() == 'image'

    formatted_string = '<a href="{url}"><img src={url}></a>' if attachment_is_image \
        else '<a href="{url}">{name}</a>'

    return mark_safe(formatted_string.format(**attachment_data))
