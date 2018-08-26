from django.core.management.base import BaseCommand

from trello_webhooks.models import CallbackEvent


class Command(BaseCommand):
    help = 'Retroactively adds the attachment type to all relevant CallbackEvents.'

    def handle(self, *args, **options):
        """Set the attachment for all Callback events in the database."""

        events = CallbackEvent.objects.filter(event_type='addAttachmentToCard')
        counter = 0

        for event in events:
            if (event.event_payload
                    .get('action')
                    .get('data')
                    .get('attachment')
                    .get('type', None)) is None:
                event.save()    # resolving the attachment type and adding to payload happens on saving.
                counter += 1

        if counter:
            self.stdout.write('Succesfully updated %s events' % counter)
        else:
            self.stdout.write('All events had an attachment type')