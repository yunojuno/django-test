# # -*- coding: utf-8 -*-


def dictget(dictionary, *keys):
    """Return dictionary data recursively."""
    return reduce(
        lambda d, key: d.get(key, None)
        if isinstance(d, dict) else None, keys, dictionary
    )
