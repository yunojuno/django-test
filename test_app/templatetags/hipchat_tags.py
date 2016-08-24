# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def render_attachment(attachment_data):
    """Render the attachment as an image if appropriate
    otherwise as link with attachment name
    """
    attachment_is_image = (
        attachment_data.get(
            'contentType', ''
        ).split('/')[0].lower() == 'image'
    )
    fmt_string = (
        '<a href="{url}"><img src="{url}"></a>' if attachment_is_image
        else '<a href="{url}">{name}</a>'
    )

    return mark_safe(fmt_string.format(**attachment_data))
