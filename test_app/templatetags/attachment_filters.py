# -*- coding: utf-8 -*-

from django import template
from django.utils.html import format_html


register = template.Library()


@register.filter
def attachment_preview(action_data):
    """Preview attachment.

    If the attachment is an image, render it as image;
    otherwise render just the name of the attachment.
    """
    content_type = action_data.get('attachmentContentType')
    if content_type and content_type.lower().startswith('image/'):
        return format_html(
            '<img src="{url}">',
            url=action_data['attachment']['url'],
        )
    else:
        return action_data['attachment']['name']
