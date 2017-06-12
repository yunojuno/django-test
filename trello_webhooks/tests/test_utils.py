# -*- coding: utf-8 -*-
from django.test import TestCase

from trello_webhooks import utils


class UtilsTests(TestCase):

    def setUp(self):
        """Set up Test Case."""
        self.test_dict = {
            'hello': 'world',
            'ham': 'jam',
            'abc': 123,
            'far': {
                'far': {
                    'away': 'land'
                }
            }
        }

    def test_dictget_dictionary_data_retrieval(self):
        """Test dictget util recursive data retrieval."""
        self.assertEqual(utils.dictget(self.test_dict, 'hello'), 'world')
        self.assertEqual(utils.dictget(self.test_dict, 'ham'), 'jam')
        self.assertEqual(utils.dictget(self.test_dict, 'abc'), 123)
        self.assertEqual(utils.dictget(self.test_dict, 'far', 'far', 'away'), 'land')
        self.assertNotEqual(utils.dictget(self.test_dict, 'a', 'b', 'c'), {})
        self.assertNotEqual(utils.dictget(self.test_dict, 'no', 'no', 'no'), 'anything')
