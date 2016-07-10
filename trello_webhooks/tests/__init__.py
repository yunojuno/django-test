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


def mock_http_request(status_code=200, headers=None):
    mock_request = mock.Mock()
    mock_request.return_value.status_code = 200
    mock_request.return_value.headers = headers or {}
    return mock.patch('requests.api.request', mock_request)
