# -*- coding: utf-8 -*-

import mock

from django.test import TestCase

from trello_webhooks.models import Webhook, CallbackEvent
from trello_webhooks.tests import get_sample_data, mock_http_request


class AttachmentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(AttachmentTest, cls).setUpClass()
        cls.webhook = Webhook().save(sync=False)

    def setUp(self):
        super(AttachmentTest, self).setUp()
        self.event = CallbackEvent(
            webhook=self.webhook,
            event_type='addAttachmentToCard',
            event_payload=get_sample_data('addAttachmentToCard', 'json'),
        )

    def test_attachment_non_image(self):
        with mock_http_request(headers={'content-type': 'application/octet-stream'}) as mock_request:
            self.event.save()
        mock_request.assert_called_once_with(
            'head',
            self.event.action_data['attachment']['url'],
            allow_redirects=False,
        )
        html = self.event.render()
        self.assertNotIn('<img ', html)

    def test_attachment_image(self):
        with mock_http_request(headers={'content-type': 'image/jpeg'}) as mock_request:
            self.event.save()
        mock_request.assert_called_once_with(
            'head',
            self.event.action_data['attachment']['url'],
            allow_redirects=False,
        )
        html = self.event.render()
        self.assertIn('<img ', html)
