# Template tags used in for the test app
from django import template

register = template.Library()


@register.filter
def content_category(content_type):
    """
    Return content 'category' from the content_type of an attachment.
    i.e. if a content_type is 'image/jpeg', then the content ceategory is 'image'
    or if if content_tpye is 'text/plain', then content category is 'text'

    This allows us to filter by content type in our templates, and use different
    markup for different types of attachments.

    Currently, only 'image' content category has its own markup defined in the
    addAttachmentToCard template, in test_app.
    All other attachment types have a link displayed.
    """
    return content_type.split("/")[0]
