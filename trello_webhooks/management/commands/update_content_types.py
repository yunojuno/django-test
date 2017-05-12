# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from trello_webhooks.models import CallbackEvent


class Command(BaseCommand):
    help = "Update the content type for all attachment CallbackEvent "

    def handle(self, *args, **options):
        """
        Filter all CallbackEvent with event_type='addAttachmentToCard'
        Add content-type of attachment to event_payload.
        """
        self.stdout.write('Start updating')
        events = CallbackEvent.objects.filter(event_type='addAttachmentToCard')
        self.stdout.write('CallbackEvent with event_type="addAttachmentToCard": {}'.format(events.count()))
        for event in events:
            event.save()
        self.stdout.write('Finished updating')
