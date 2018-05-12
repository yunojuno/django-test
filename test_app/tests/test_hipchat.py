# -*- coding: utf-8 -*-
import mock

from django.test import TestCase

from test_app import hipchat


class HipChatTests(TestCase):

    @mock.patch("requests.post")
    def test_hipchat(self, mock_post):
        mock_post.return_value = mock.MagicMock(status_code=200)
        hipchat.send_to_hipchat("testing")
        self.assertEqual(mock_post.call_count, 1)
