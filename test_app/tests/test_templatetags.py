from django.test import TestCase

from test_app.templatetags.test_app_filters import solve_attachment_type
from trello_webhooks.tests import get_sample_data

class TemplateTagsTests(TestCase):

    def setUp(self):
        self.data = get_sample_data('addAttachmentToCard', 'json')
        self.data = self.data['action']['data']['attachment']

    def test_solve_attachment_type(self):
        self.data['type'] = 'image'
        url = 'https://trello-attachments.s3.amazonaws.com/4f7dcc310113192a307f347d/1294x1268/219cc6eb9c9b7b2ef8b1251c90a4184a/trello-logo.png'
        self.assertEqual(solve_attachment_type(self.data), '<img src=%s>' % url)

        self.data['type'] = 'text'
        self.assertEqual(solve_attachment_type(self.data), 'trello-logo.png')