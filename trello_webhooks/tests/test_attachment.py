# -*- coding: utf-8 -*-
"""
    Test Attachment Content-Type and Attachment rendering
"""
import json
from django.core.urlresolvers import reverse
from django.test import TestCase
from trello_webhooks.models import Webhook, CallbackEvent
from trello_webhooks.tests import get_sample_data


class AttachmentTests(TestCase):
    """
        Test Attachment rendering
    """

    def setUp(self):
        """
        Setup test case
        Returns: None

        """
        self.payload = {'auth_token': 'A', 'trello_model_id': '123'}
        self.url = reverse('trello_callback_url', kwargs=self.payload)
        self.event_type = 'addAttachmentToCard'

    def test_post_card_with_attachment(self):
        """
        Test Post Card with attachment (png)
        Attachment must be not None
        <img> tag must be included in rendered html
        Returns: None
        """
        Webhook(
            auth_token=self.payload['auth_token'],
            trello_model_id=self.payload['trello_model_id']
        ).save(sync=False)

        # No callback events after create Webhook
        self.assertEqual(CallbackEvent.objects.count(), 0)
        test_payload = get_sample_data(self.event_type, 'json')

        resp = self.client.post(
            self.url,
            data=json.dumps(test_payload),
            content_type='application/json'
        )

        self.assertEqual(resp.status_code, 200)
        # Callback event on send request to callback url
        self.assertEqual(CallbackEvent.objects.count(), 1)

        callback_event = CallbackEvent.objects.get()

        self.assertEquals(callback_event.attachment['content_type'], 'image/jpeg')
        # Check if <img> tag rendered
        self.assertIn('<img src="{}"/>'.format(callback_event.attachment['url']), callback_event.render())
