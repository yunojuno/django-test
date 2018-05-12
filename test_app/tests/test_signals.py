# -*- coding: utf-8 -*-
import mock

from django.test import TestCase

from test_app.signals import (
    get_supported_events,
)


class SignalTest(TestCase):

    def test_get_supported_events(self):
        good = get_supported_events()
        self.assertTrue("updateComment" in good)
        self.assertTrue("addAttachmentToCard" in good)
