# -*- coding: utf-8 -*-
from django.test import TestCase


from test_app.templatetags.test_app_tags import content_category


class TemplateTagTests(TestCase):
    """ Test to ensure content category is returned """
    def test_content_category(self):
    	content_type = "image/jpeg"
        self.assertEqual("image", content_category(content_type))