from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def render_card_attachment(attachment):
    content_type = attachment.get('mimeType') or 'unknown'

    if content_type.startswith('image/'):
        # show image title with a link and image itself below
        attachment_template = (
            '"<strong><a href="{url}">{name}</a></strong>"'
            '<br/><a href="{url}"><img src="{url}" alt="{name}"/></a>'
        )
    else:
        attachment_template = '"<strong><a href="{url}">{name}</a></strong>"'

    return mark_safe(attachment_template.format(
        url=conditional_escape(attachment.get('url', '')),
        name=conditional_escape(attachment.get('name', '')),
    ))
