# -*- coding: utf-8 -*-
from django.test import TestCase

from test_app.templatetags import filters


class FiltersTests(TestCase):

    def test_content_type_with_image(self):
        attachment = {
            'name': 'Screenshot.png',
            'url': 'https://test.org',
            'content_type': 'image/png',
        }
        self.assertEqual(
            filters.render_attachment(attachment),
            '<a href="https://test.org"><img src="https://test.org"></a>'
        )

    def test_content_type_with_video(self):
        attachment = {
            'name': 'sail.mp4',
            'url': 'https://test.org',
            'content_type': 'video/mp4',
        }
        self.assertEqual(
            filters.render_attachment(attachment),
            '<a href="https://test.org">sail.mp4</a>'
        )