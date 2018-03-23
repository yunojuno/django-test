from ddt import ddt, data
from django.test import TestCase

from test_app.templatetags.card_attachment_text import card_attachment_text


@ddt
class CardAttachmentTextTest(TestCase):
    @data(
        'image/gif',
        'image/png',
        'image/jpeg',
        'image/bmp',
        'image/webp',
    )
    def test_supported_image_content_type(self, content_type):
        data = {
            'attachment': {
                'name': 'file.name',
                'content_type': content_type,
                'previewUrl': 'previewUrl'
            }
        }

        expected_result = u'<img src="previewUrl">'

        result = card_attachment_text(data)

        self.assertEqual(expected_result, result)

    @data(
        '',
        'my_awesome_type',
        'image/tiff',
        'text/plain',
    )
    def test_unsopported_content_type(self, content_type):
        data = {
            'attachment': {
                'name': 'file.name',
                'content_type': content_type,
                'previewUrl': 'previewUrl'
            }
        }

        expected_result = 'file.name'

        result = card_attachment_text(data)

        self.assertEqual(expected_result, result)
