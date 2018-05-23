from django.test import TestCase

from test_app.templatetags.attachment_parsing import is_image


class IsImageTestCase(TestCase):

    def test_is_image_true(self):
        self.assertTrue(is_image('image/jpeg'))

    def test_is_image_false(self):
        self.assertFalse(is_image('application/pdf'))
