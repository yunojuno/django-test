from django.test import TestCase

from test_app.templatetags import render_filters


class RenderAttachmentTests(TestCase):

    def test_image_content_type(self):
        attachment = {
            'name': 'example.png',
            'url': 'https://www.example.com/example.png',
            'mimeType': 'image/png',
        }
        self.assertEqual(
            render_filters.render_attachment(attachment),
            '<img src="https://www.example.com/example.png" alt="example.png">'
        )

    def test_undefined_content_type(self):
        attachment = {
            'name': 'undefined',
            'url': 'https://www.example.com/undefined',
            'mimeType': None,
        }
        self.assertEqual(
            render_filters.render_attachment(attachment),
            '"undefined"'
        )

    def test_unknown_content_type(self):
        attachment = {
            'name': 'example.html',
            'url': 'https://www.example.com/example.html',
            'mimeType': 'text/html',
        }
        self.assertEqual(
            render_filters.render_attachment(attachment),
            '"example.html"'
        )
