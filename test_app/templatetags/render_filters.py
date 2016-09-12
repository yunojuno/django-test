from django import template
from django.utils.html import format_html


register = template.Library()


@register.filter
def render_attachment(attachment):
    """Render a Trello attachment as HTML.

    If the content type is supported, this will render the attachment
    with the known renderer; if not, it will simply render its name.
    """
    content_type = attachment.get('mimeType', '')
    url = attachment.get('url', '')
    name = attachment.get('name', '')
    if content_type and content_type.startswith('image/'):
        return format_html('<img src="{}" alt="{}">', url, name)
    return '"{}"'.format(name)
