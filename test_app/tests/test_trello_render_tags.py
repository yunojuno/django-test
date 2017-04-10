from django.test import TestCase
from django.template import Template, Context


class TrelloAttachmentRenderTestcase(TestCase):

    def test_render_card_attachment(self):
        template = Template(
            '{% load trello_render_tags %}'
            '{{ attach|render_card_attachment }}'
        )
        test_img_attaches = [
            {'url': 'https://some.domain/img.png', 'name': 'attach', 'mimeType': 'image/png'},
            {'url': 'https://some.domain/img.jpg', 'name': 'attach', 'mimeType': 'image/jpeg'},
        ]
        test_other_attaches = [
            {'url': 'https://some.domain/img.mp4', 'name': 'attach', 'mimeType': 'video/mp4'},
            {'url': 'https://some.domain/img.html', 'name': 'attach', 'mimeType': 'html/text'},
            {'url': 'https://some.domain/img.html', 'name': 'attach', 'mimeType': None},
            {'url': 'https://some.domain/img.html', 'name': 'attach'},
        ]

        for test_attach in test_img_attaches:
            self.assertTrue('<img' in template.render(Context({'attach': test_attach})))

        for test_attach in test_other_attaches:
            self.assertFalse('<img' in template.render(Context({'attach': test_attach})))
