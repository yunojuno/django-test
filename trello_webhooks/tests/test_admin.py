# -*- coding: utf-8 -*-
import mock

from django.test import TestCase, RequestFactory

from trello_webhooks.admin import CallbackEventAdmin, CallbackEventInline, WebhookAdmin
from trello_webhooks.models import Webhook, CallbackEvent
from trello_webhooks.tests import get_sample_data


class CallbackEventAdminTests(TestCase):

    def setUp(self):
        self.webhook = Webhook(auth_token='ABC').save(sync=False)
        self.event = CallbackEvent(
            webhook=self.webhook,
            event_type='commentCard',
            event_payload=get_sample_data('commentCard', 'json')
        ).save()
        self.admin = CallbackEventAdmin(CallbackEvent, None)

    def test_webhook_(self):
        self.assertEqual(
            self.admin.webhook_(self.event),
            self.webhook.id
        )

    def test_title_length(self):
        # admin shows up to 3 words of board, list and card names
        self.event.board['name'] = 'First Second Third Forth'
        self.event.list['name'] = 'First Second Third Forth'
        self.event.card['name'] = 'First Second Third Forth'

        self.assertEqual(self.admin.board_(self.event), 'First Second Third ...')
        self.assertEqual(self.admin.list_(self.event), 'First Second Third ...')
        self.assertEqual(self.admin.board_(self.event), 'First Second Third ...')

    def test_payload_(self):
        self.event.event_payload = {'test': 'value'}
        self.assertEqual(
            self.admin.payload_(self.event),
            '<code>{\n&nbsp;&nbsp;&nbsp;&nbsp;"test":&nbsp;"value"\n}</code>'
        )

    def test_has_template(self):
        self.assertTrue(self.admin.has_template(self.event))
        self.event.event_type = 'X'
        self.assertFalse(self.admin.has_template(self.event))

    def test_rendered(self):
        self.assertIsNotNone(self.admin.rendered(self.event))
        self.event.event_type = 'X'
        self.assertIsNone(self.admin.rendered(self.event))


class CallbackEventInlineTests(TestCase):

    def setUp(self):
        self.webhook = Webhook(auth_token='ABC').save(sync=False)
        self.event = CallbackEvent(
            webhook=self.webhook,
            event_type='commentCard',
            event_payload=get_sample_data('commentCard', 'json')
        ).save()
        self.admin = CallbackEventInline(CallbackEvent, None)

    def test_action_taken_by(self):
        self.event.member['fullName'] = 'Member Name'
        self.assertEqual(self.admin.action_taken_by(self.event), 'Member Name')

    def test_timestamp_(self):
        # shows as a link
        self.assertRegexpMatches(self.admin.timestamp_(self.event), r'<a href="[^"]+">.+</a>')

    def test_rendered(self):
        self.assertIsNotNone(self.admin.rendered(self.event))
        self.event.event_type = 'X'
        self.assertIsNone(self.admin.rendered(self.event))


class WebhookAdminTests(TestCase):

    def setUp(self):
        self.webhook = Webhook(auth_token='ABC').save(sync=False)
        self.admin = WebhookAdmin(Webhook, None)

    def test_auth_token_(self):
        # admin shows upto 12 chars of auth_token
        self.webhook.auth_token = 'abcdef' * 10
        self.assertEqual(self.admin.auth_token_(self.webhook), 'abcdefabc...')

    def test_sync(self):
        request = RequestFactory().get('/test')
        request.user = None

        with mock.patch('trello_webhooks.models.Webhook.sync') as sync_mock:
            self.admin.sync(request, Webhook.objects.all())
            self.assertEqual(sync_mock.call_count, 1)

        with mock.patch('trello_webhooks.models.Webhook.sync') as sync_mock:
            self.admin.sync(request, Webhook.objects.none())
            self.assertEqual(sync_mock.call_count, 0)
