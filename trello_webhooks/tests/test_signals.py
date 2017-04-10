# -*- coding: utf-8 -*-
import mock

from django.test import TestCase

from trello_webhooks.models import Webhook
from trello_webhooks.signals import callback_received
from trello_webhooks.tests import get_sample_data


class TrelloWebhooksSignalsTestCase(TestCase):

    def test_callback_received_signal(self):
        """Checks that `callback_received` is fired after catching new event by webhook"""

        receiver = mock.Mock()
        callback_received.connect(receiver)
        self.assertEqual(receiver.call_count, 0)

        hook = Webhook().save(sync=False)
        event = hook.add_callback(get_sample_data('createCard', 'text'))

        callback_received.disconnect(receiver)
        self.assertEqual(receiver.call_count, 1)
