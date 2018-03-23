from django import template
from django.utils.safestring import mark_safe

register = template.Library()

SUPPORTED_CONTENT_TYPES = {
    'images': {
        'content_types': [
            'image/gif',
            'image/png',
            'image/jpeg',
            'image/bmp',
            'image/webp',
        ],
        'template': '<img src="%s">',
    },
}


@register.filter
def card_attachment_text(data):
    attachment = data.get('attachment', {})
    result = '%s' % (attachment.get('name'),)

    content_type = attachment.get('content_type')

    for supported_type, item in SUPPORTED_CONTENT_TYPES.iteritems():
        if content_type in item['content_types']:
            result = item['template'] % (attachment.get('previewUrl'),)

    return mark_safe(result)
