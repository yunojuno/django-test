from django.template.loader_tags import register
from django.utils.html import format_html


@register.filter
def render_attachment(attachment):
    """Render attachment to correct html according content type"""
    content_type = attachment.get('content_type', '')
    if content_type.startswith('image/'):
        html = '<a href="{url}"><img src={url}></a>'
    else:
        html = '<a href="{url}">{name}</a>'

    return format_html(html, **attachment)