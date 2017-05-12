from mock import patch, PropertyMock

from test_app.hipchat import send_to_hipchat
from unittest import TestCase


class SendToHipChatTest(TestCase):

    @patch('test_app.hipchat.requests.post')
    def test_sending_message_to_hipchat(self, m_post):
        m_post.return_value = PropertyMock(status_code=200)
        self.assertEqual(send_to_hipchat('test'), 200)
        self.assertEqual(m_post.call_count, 1)
        args, kwargs = m_post.call_args
        self.assertDictEqual(
            kwargs['json'],
            {
                'color': 'yellow',
                'from': 'Trello',
                'message': 'test',
                'message_format': 'html',
                'notify': False
            }
        )
        self.assertDictEqual(
            kwargs['headers'],
            {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer None'
            }
        )
