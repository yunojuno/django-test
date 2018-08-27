from django.test import TestCase
from test_app.hipchat import send_to_hipchat

import mock
import requests


class HipChatTest(TestCase):

    def test_send_to_hipchat(self):
        with mock.patch.object(requests, 'post') as post_mock:
            post_mock.return_value = mock_response = mock.Mock()
            mock_response.status_code = 123
            input_payload = {
                'message': 'Hello yunojuno',
                'token': 'token',
                'room': 'room',
                'sender': 'Trello',
                'color': 'yellow',
                'notify': False
            }

            payload = {
                'auth_token': 'token',
                'notify': False,
                'color': 'yellow',
                'from': 'Trello',
                'room_id': 'room',
                'message': 'Hello yunojuno'
            }

            self.assertEqual(send_to_hipchat(**input_payload), 123)
            post_mock.assert_called_with('https://api.hipchat.com/v1/rooms/message', data=payload)