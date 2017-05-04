import json
from os import path


def get_sample_data(action):
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
        return json.load(f)
