# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.management import call_command

from trello_webhooks.models import Webhook, CallbackEvent
from trello_webhooks.tests import get_sample_data, mock_http_request


class ManagementTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ManagementTest, cls).setUpClass()
        cls.webhook = Webhook().save(sync=False)

    def test_resolve_attachment_type(self):
        ce = CallbackEvent(
            webhook=self.webhook,
            event_type='addAttachmentToCard',
            event_payload=get_sample_data('addAttachmentToCard', 'json'),
        )
        with mock_http_request(status_code=404) as mock_request:
            ce.save()
        mock_request.assert_called_once_with(
            'head',
            ce.action_data['attachment']['url'],
            allow_redirects=False,
        )
        self.assertNotIn('attachmentContentType', ce.action_data)
        with mock_http_request(headers={'content-type': 'image/x-unique-test-type'}) as mock_request:
            call_command('resolve_attachment_type')
        mock_request.assert_called_once_with(
            'head',
            ce.action_data['attachment']['url'],
            allow_redirects=False,
        )
        ce = CallbackEvent.objects.get(pk=ce.pk)
        self.assertIn('attachmentContentType', ce.action_data)
        self.assertEqual(
            'image/x-unique-test-type',
            ce.action_data['attachmentContentType'],
        )
