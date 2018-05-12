# # -*- coding: utf-8 -*-
# update content_type with all existing CallbackEvent in database
from optparse import make_option
import logging
import time

from django.core.management.base import BaseCommand

from trello_webhooks.models import CallbackEvent

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = u"Update 'content_type' with existing CallbackEvent in database."
    option_list = BaseCommand.option_list + (
        make_option(
            "-w",
            "--wait",
            dest="wait",
            default=200,
            help=u"Run command in wait mode (default 200), pause betweek calls"
        ),
    )

    def handle(self, *args, **options):
        """Update 'content_type' with existing CallbackEvent in database.

        Since 'content_type' is determined by issuing a HEAD requests call to
        attachment's url, this could be an expensive operation if we go
        through all database records.

        You can set the 'wait' parameter with '--wait' flag, with the given
        'wait' time (in ms), it will pause between each HEAD requests call.

        Updated records will not be touched again, so it is safe to run this
        command multiple times.
        """

        logger.info(
            u"Querying CallbackEvent with attachment but missing content_type"
        )
        ces = CallbackEvent.objects.filter(
            event_payload__contains='"attachment":'
        ).exclude(
            event_payload__contains='"content_type":'
        )

        wait = options["wait"]
        success_count = 0

        # Using iterator here to avoid unnecessary result caching
        for ce in ces.iterator():
            # this will call update_callbackevent_content_type
            ce.save(update_fields=["event_payload"])
            success_count += 1
            logger.info(
                u"Updated %s successfully with '%s'",
                repr(ce), ce.attachment.get("content_type")
            )
            # if 'wait' time (ms) is set, let's take a pause
            wait and time.sleep(wait)

        logger.info(u"Total %d records updated", success_count)
