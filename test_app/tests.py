from django.template import Template, Context
from django.test import TestCase


class TestHipchatTags(TestCase):
    TEMPLATE = Template("{% load hipchat %} {{ attachment|render_attachment }}")

    def test_render_attachment(self):
        attachment = {'url': 'http://test',
                      'name': 'test-name',
                      'content_type': 'test'}
        rendered = self.TEMPLATE.render(Context({'attachment': attachment}))

        self.assertIn('test-name', rendered)

        attachment = {'url': 'http://test',
                      'name': 'test-name',
                      'content_type': 'image/png'}
        rendered = self.TEMPLATE.render(Context({'attachment': attachment}))
        self.assertIn('img', rendered)
