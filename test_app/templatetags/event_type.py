from django import template


register = template.Library()


@register.filter()
def attachment_link(data):
    """
    Return url of attachment depending on the type
    """
    content_type = data.get('content_type', None)
    url = data.get('url', '')
    if content_type and content_type.split('/')[0] == 'image':
        return '<img src="{url}">'.format(url=url)
    return url
