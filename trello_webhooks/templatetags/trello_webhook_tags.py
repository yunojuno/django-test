# Template tags used in BackOffice only
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def trello_api_key():
    """Return TRELLO_API_KEY for use in templates."""
    return settings.TRELLO_API_KEY


@register.filter
def trello_updates(new, old):
    """Parse out the updates from Trello payload.

    Best explained by an example: when a list is moved, an updateList
    event is fired, and the payload from Trello contains the following
    in the action.data node:

    {
        "list":{
            "id": "5476fc06d998c88c890b901d",
            "pos": 131071,
            "name": "Second list"
        },
        "old":{
            "pos": 262143
        }
    }

    From this, we can work out that the field that has changed is 'pos',
    as it's in the 'old' dict, and that its value has changed from
    262143 to 131071

    The output from this tag would therefore be:

    {"pos": (262143, 131071)}

    Args:
        new: dict, the complete node in its current state
        old: dict, the 'old' node against which to compare

    Returns: a dictionary containing the fields that have
        changed as the keys, and a 2-tuple as the value
        containing old, new values of the field.

    """
    try:
        return {k: (v, new[k]) for k, v in old.iteritems()}
    except KeyError:
        return {k: (v, None) for k, v in old.iteritems()}


@register.filter
def render_attachment(attachment):
    """Render attachment with an img tag if it's an image, otherwise
    just return a link.
    """
    if attachment['contenttype'].split('/')[0] == 'image':
        # Wrap the url with img tag
        return mark_safe(
            '<a href="%(url)s" target="_blank><img src="%(url)s"></a>' % {'url': attachment['url']}
        )

    return mark_safe(
        '<strong><a href="%(url)s" target="_blank>%(url)s</a></strong>' % {'url': attachment['url']}
    )
