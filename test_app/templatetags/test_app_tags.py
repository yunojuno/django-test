from django.template.loader_tags import register
from django.utils.html import format_html


@register.filter
def render_attachment(attachment):
    """Render attachment depending on it's content-type"""
    content_type = attachment.get('content_type', '')
    if content_type.startswith('image/'):
        return format_html('<a href="{url}"><img src="{url}"></a>',
                           **attachment)
    else:
        return format_html('<a href="{url}">{name}</a>',
                           **attachment)
