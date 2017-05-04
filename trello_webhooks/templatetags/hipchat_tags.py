# -*- coding: utf-8 -*-
from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter
def hipchat_attachment(attachment):
    content_type = attachment.get('content_type', '')

    if content_type.startswith('image/'):
        html = '<a href="{url}"><img src="{url}"></a>'
    else:
        html = '<a href="{url}">{name}</a>'

    return format_html(html, **attachment)
