from unittest import TestCase
from test_app.signals import get_supported_events


class SignalsTest(TestCase):

    def test_supported_events(self):
        self.assertEqual(get_supported_events(), ['updateComment'])
