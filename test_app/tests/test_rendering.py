from django.template import Template, Context
from django.test import TestCase


class TestHipchatTags(TestCase):
    TEMPLATE = Template("{% load hipchat_tags %} {{ attachment|render_attachment }}")

    def test_rendering_image_attachment(self):
        attachment = {'url': 'http://test_image_attachment',
                      'name': 'test',
                      'content_type': 'image/png'}
        html = self.TEMPLATE.render(Context({'attachment': attachment}))
        self.assertIn('img', html)
        self.assertIn(attachment['url'], html)
        self.assertIn(attachment['name'], html)

    def test_rendering_non_image_attachment(self):
        attachment = {'url': 'http://test_non_image_attachment',
                      'name': 'test',
                      'content_type': 'text/html'}
        html = self.TEMPLATE.render(Context({'attachment': attachment}))
        self.assertNotIn('img', html)
        self.assertIn(attachment['name'], html)
        self.assertIn(attachment['url'], html)