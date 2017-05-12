# -*- coding: utf-8 -*-
from django.conf import settings

import requests

HIPCHAT_API_URL = 'https://api.hipchat.com/v2/room/{room}/notification'


def send_to_hipchat(
        message,
        token=settings.HIPCHAT_API_TOKEN,
        room=settings.HIPCHAT_ROOM_ID,
        sender="Trello",
        color="yellow",
        notify=False,
        message_format="html"):
    """
    Send a message to HipChat.

    Returns the status code of the request. Should be 200.
    """
    payload = {
        "notify": notify,
        "color": color,
        "message_format": message_format,
        "message": message,
        "from": sender
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {token}'.format(token=token),
    }
    return requests.post(HIPCHAT_API_URL.format(room=room), json=payload, headers=headers).status_code
