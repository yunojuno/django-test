import mimetypes

import requests


def calculate_content_type(url):
    """Attempts to work out the content type (mimetype) of a given URL.

    First we rely on guessing the mimetype from the extension, to save use
    a sync HTTP request. If that fails, we try a HEAD request to retrieve
    the content type from the server without downloading the entire file.

    NB: mimetype lookup by extension can be unreliable but for this use
    case the level of reliability is better than firing a request every time.
    """
    content_type = mimetypes.guess_type(url)[0]
    if not content_type:
        return retrieve_content_type(url)
    return content_type


def retrieve_content_type(url):
    """Calculate a URLs content-type by visiting it with a HEAD request."""
    try:
        response = requests.head(url)
    except requests.RequestException:
        return ''
    else:
        content_type = response.headers.get('content-type')
        return content_type
