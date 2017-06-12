# -*- coding: utf-8 -*-
import responses
from unittest import TestCase
from test_app import hipchat


class HipchatTests(TestCase):

    @responses.activate
    def test_send_to_hipchat_method(self):
        responses.add(
            responses.POST, 'https://api.hipchat.com/v1/rooms/message',
            body='',
            status=200)
        response = hipchat.send_to_hipchat(message='test123')
        self.assertEqual(response, 200)
