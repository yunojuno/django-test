# trello_webhooks.tests package
import json
from os import path
import mock


def get_sample_data(action, format_):
    """Return test JSON payload as 'json' or 'text' object.

    Args:
        action: string, one of the filenames, without the extension,
            e.g. 'commentCard', 'createCard' etc. Look in sample_data/
            for the full list
        format_: string, one of either 'json' or 'text'
    """
    _path = path.join(
        path.abspath(path.dirname(__file__)),
        'sample_data/%s.json' % action
    )
    with open(_path, 'r') as f:
        return f.read() if format_ == 'text' else json.load(f)


def get_mock_response(content_type):
    response = mock.MagicMock()
    response.headers = {'Content-Type': content_type}
    return response