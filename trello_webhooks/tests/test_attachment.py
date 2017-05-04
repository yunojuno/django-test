# -*- coding: utf-8 -*-
"""
    Test Attachment Content-Type and Attachment rendering
"""
import json
from django.core.urlresolvers import reverse
from django.test import TestCase
from trello_webhooks.models import Webhook, CallbackEvent
from trello_webhooks.tests import get_sample_data
import mock
from requests import Response
from bs4 import BeautifulSoup


def _get_response(content_type):
    """
    Get requests.Response and set Content-Type
    Args:
        content_type: string
    Returns:
        requests.Response
    """
    resp = Response()
    resp.headers['Content-Type'] = content_type
    resp.status_code = 200
    return resp


def mock_image_request(*args, **kwargs):
    """
    Make fake mock request
    Content-Type is image
    Returns:
        requests.Response instance
    """
    return _get_response('image/jpeg')


def mock_pdf_request(*args, **kwargs):
    """
    Make fake mock request
    Content-Type is pdf
    Returns:
        requests.Response instance
    """
    return _get_response('application/pdf')


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
        self.image_tag_name = 'img'
        self.image_src_attr = 'src'

    @mock.patch('requests.head', mock_image_request)
    def test_render_attachment_image(self):
        """
        Test Post Card with attachment (png)
        <img> tag must be included in rendered html
        Returns: None
        """
        self._send_webhook()
        # Callback event created on send request to callback url
        self.assertEqual(CallbackEvent.objects.count(), 1)

        callback_event = CallbackEvent.objects.get()
        # Check content type - must be image/jpeg
        self.assertEquals(callback_event.attachment['content_type'], 'image/jpeg')

        # load rendered html as BeautifulSoap instance
        rendered_html = BeautifulSoup(callback_event.render())
        img_tag = rendered_html.find(self.image_tag_name)

        # Check if <img> tag rendered
        self.assertIsNot(img_tag, None)
        # Check src attribute of the img tag
        self.assertEquals(img_tag.get(self.image_src_attr), callback_event.attachment['url'])

    @mock.patch('requests.head', mock_pdf_request)
    def test_attachment_not_image(self):
        """
        Test attachment not image
        No image tag should be in rendered template
        Returns:
            None
        """
        self._send_webhook()

        callback_event = CallbackEvent.objects.get()
        # content type is not image
        self.assertNotIn('image', callback_event.attachment['content_type'])

        rendered_html = BeautifulSoup(callback_event.render())
        img_tag = rendered_html.find(self.image_tag_name)
        # img tag shouldn't be rendered
        self.assertIs(img_tag, None)

    def _send_webhook(self):
        """
        Create webhook and create callback event
        Returns:
            None
        """
        Webhook(
            auth_token=self.payload['auth_token'],
            trello_model_id=self.payload['trello_model_id']
        ).save(sync=False)
        self.assertEqual(CallbackEvent.objects.count(), 0)

        test_payload = get_sample_data(self.event_type, 'json')

        resp = self.client.post(self.url, data=json.dumps(test_payload),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
