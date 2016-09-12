from mock import patch

import responses
from requests.exceptions import HTTPError

from django.test import TestCase
from trello_webhooks import attachments


@patch.object(attachments, 'retrieve_content_type')
class CalculateContentTypeTests(TestCase):

    def test_calculate_content_type_with_known_extension(
            self, mocked_retrieve_content_type):
        url = "https://www.example.com/example.jpg"
        content_type = attachments.calculate_content_type(url)
        self.assertEqual(content_type, "image/jpeg")
        self.assertFalse(mocked_retrieve_content_type.called)

    def test_calculate_content_type_with_missing_extension(
            self, mocked_retrieve_content_type):
        mocked_retrieve_content_type.return_value = "image/png"
        url = "https://www.example.com/example"
        content_type = attachments.calculate_content_type(url)
        self.assertEqual(content_type, "image/png")
        mocked_retrieve_content_type.assert_called_once_with(url)


class RetrieveContentTypeTests(TestCase):

    @responses.activate
    def test_successful_retrieval(self):
        url = "https://www.example.com/example.png"
        responses.add(responses.HEAD, url, status=200, content_type='image/png')
        content_type = attachments.retrieve_content_type(url)
        self.assertEqual(content_type, 'image/png')

    @responses.activate
    def test_retrieval_raises_exception(self):
        url = "https://www.example.com/example.png"
        exception = HTTPError('Timeout or something')
        responses.add(responses.HEAD, url, body=exception)
        content_type = attachments.retrieve_content_type(url)
        self.assertEqual(content_type, '')
