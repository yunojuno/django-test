# -*- coding: utf-8 -*-
from django.conf import settings

import requests

# Use v2 API, see docs: https://www.hipchat.com/docs/apiv2
HIPCHAT_API_URL = 'https://api.hipchat.com/v2/'


def send_to_hipchat(
        message,
        token=settings.HIPCHAT_API_TOKEN,
        room=settings.HIPCHAT_ROOM_ID,
        sender="Trello",
        color="yellow",
        notify=False):
    """
    Send a message to HipChat.

    Returns the status code of the request. Should be 200.
    """
    payload = {
        'auth_token': token,
        'notify': notify,
        'color': color,
        'from': sender,
        'message': message
    }
    return requests.post(
        # This is old style string formatting, it's not worth refactoring
        # really but when working on greenfield stuff should be avoided.
        HIPCHAT_API_URL + 'room/%s/notification' % room, data=payload
    ).status_code
