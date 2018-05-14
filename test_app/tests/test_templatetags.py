# -*- coding: utf-8 -*-
from django.test import TestCase

from test_app.templatetags.trello_callbackevent_tags import (
    attachment_name_or_inline_image,
)


class TemplateTagTests(TestCase):

    def test_attachment_name_or_inline_image(self):
        attachment_name = 'attachment_name'
        attachment_url = 'attachment_url'
        safe_image_tag = '<img src="%s" alt="%s">' % (
            attachment_url, attachment_name
        )
        # good data: with image
        good = {
            'name': attachment_name,
            'url': attachment_url,
            'content_type': 'image/png'
        }
        self.assertEqual(
            attachment_name_or_inline_image(good),
            safe_image_tag
        )

        # bad data missing content_type: with name
        bad_missing_content_type = {
            'name': attachment_name,
            'url': attachment_url
        }
        self.assertEqual(
            attachment_name_or_inline_image(bad_missing_content_type),
            attachment_name
        )

        # bad data non-image content_type: with name
        bad_non_image_content_type = {
            'name': attachment_name,
            'url': attachment_url,
            'content_type': 'text/plain'
        }
        self.assertEqual(
            attachment_name_or_inline_image(bad_non_image_content_type),
            attachment_name
        )
