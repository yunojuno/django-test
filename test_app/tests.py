# -*- coding: utf-8 -*-
import mock

from django.test import TestCase

from test_app.hipchat import send_to_hipchat


class mock_requests_post_return_value:
    """
    Fake return value for the mocked requests.post
    """
    status_code = 200


class HipchatTests(TestCase):

    @mock.patch("requests.post", return_value=mock_requests_post_return_value)
    def test_send_to_hipchat(self, mock_post):
        # Check correct information is passed on to requests.post
        args = {'token': 'abc',
                'room': 'def',
                'color': 'ghi',
                'sender': 'jkl',
                'notify': 'mno'}

        payload = {
            'auth_token': 'abc',
            'notify': 'mno',
            'color': 'ghi',
            'from': "jkl",
            'room_id': "def",
            'message': "xyz"
        }

        send_to_hipchat("xyz", **args)
        mock_post.assert_called_with(
                    'https://api.hipchat.com/v1/rooms/message',
                    data=payload)
