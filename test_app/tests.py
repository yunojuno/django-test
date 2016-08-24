# -*- coding: utf-8 -*-
import mock

from django.test import TestCase

from trello_webhooks.models import Webhook, CallbackEvent
from trello_webhooks.tests import (
    get_sample_data,
    MockRequestResponse
)


class HipChatTests(TestCase):

    @mock.patch('trello_webhooks.models.requests.get')
    def test_render_image_attachment(self, mocked_requests_get):
        # create a mock for requests
        # only interested in the Content-Type
        mr = MockRequestResponse({'Content-Type': 'image/png'})
        mocked_requests_get.return_value = mr
        hook = Webhook(trello_model_id="M", auth_token="A").save(sync=False)
        ce = CallbackEvent(webhook=hook, event_type='addAttachmentToCard')
        ce.event_payload = get_sample_data('addAttachmentToCard', 'text')
        ce.save()
        rendered_html = ce.render()
        self.assertInHTML(
            '<img src="http://test/media/blah.png">',
            rendered_html
        )

    @mock.patch('trello_webhooks.models.requests.get')
    def test_render_non_image_attachment(self, mocked_requests_get):
        # create a mock for requests
        # only interested in the Content-Type
        mr = MockRequestResponse({'Content-Type': 'application/pdf'})
        mocked_requests_get.return_value = mr
        hook = Webhook(trello_model_id="M", auth_token="A").save(sync=False)
        ce = CallbackEvent(webhook=hook, event_type='addAttachmentToCard')
        ce.event_payload = get_sample_data('addAttachmentToCard', 'text')
        ce.save()
        rendered_html = ce.render()
        # pdf named as .png!
        self.assertInHTML(
            '<a href="http://test/media/blah.png">blah.png</a>',
            rendered_html
        )
