import logging

from django.core.management.base import BaseCommand

from trello_webhooks.models import CallbackEvent


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Resolves content types of existing events, if they have an attachment."

    def handle(self, *args, **kwargs):
        callback_events = CallbackEvent.objects.filter(event_type="addAttachmentToCard")
        for callback_event in callback_events:
            logger.info("Processing event: %s", callback_event)
            callback_event.save()
        logger.info("Finished.")
