# -*- coding: utf-8 -*-
# retrospectively add the content type of all the attachments added so far
import logging

from django.core.management.base import BaseCommand

from trello_webhooks.models import CallbackEvent

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Add the content type of all the attachments added so far."

    def handle(self, *args, **options):
        """For each CallbackEvent of event_type addAttachmentToCard
        update the event_payload so the attachment content-type
        is inserted into the JSON
        Should only need to be run once to enhance existing events
        """
        attachment_callback_events = CallbackEvent.objects.filter(
            event_type='addAttachmentToCard'
        )
        for event in attachment_callback_events:
            logger.info(u"Updating (%r)", event)
            event.save()
