# -*- coding: utf-8 -*-
from django.template import Context, Template
from django.test import TestCase


class TestTemplateTags(TestCase):

    template = Template("{% load hipchat_tags %} {{ attachment|render_attachment }}")

    def test_render_image_attachment(self):
        image_attachment = {
            'url': 'http://test.com',
            'name': 'test-image',
            'content_type': 'image/png'
        }
        rendered_template = self.template.render(Context({'attachment': image_attachment}))
        self.assertIn('img', rendered_template)
        self.assertIn(image_attachment['url'], rendered_template)

    def test_render_not_image_attachment(self):
        not_image_attachment = {
            'url': 'http://test.com',
            'name': 'some-document',
            'content_type': 'application/pdf'
        }
        rendered_template = self.template.render(Context({'attachment': not_image_attachment}))
        self.assertNotIn('img', rendered_template)
        self.assertIn(not_image_attachment['url'], rendered_template)
        self.assertIn(not_image_attachment['name'], rendered_template)