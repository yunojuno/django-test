from django.template import Template, Context
from django.test import TestCase


class TestHipchatTags(TestCase):
    def test_rendering_attachments(self):
        template = Template("{% load hipchat_tags %} {{ attachment|render_attachment }}")
        attachment = {'url': 'http://test_image_attachment',
                      'name': 'test',
                      'content_type': 'image/png'}
        html = template.render(Context({'attachment': attachment}))
        self.assertIn('img', html)
        self.assertIn(attachment['url'], html)
        self.assertIn(attachment['name'], html)

        attachment = {'url': 'http://test_non_image_attachment',
                      'name': 'test',
                      'content_type': 'text/html'}
        html = template.render(Context({'attachment': attachment}))
        self.assertNotIn('img', html)
        self.assertIn(attachment['name'], html)
        self.assertIn(attachment['url'], html)