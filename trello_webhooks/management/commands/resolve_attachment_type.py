# -*- coding: utf-8 -*-

import logging

from django.core.management.base import BaseCommand

from trello_webhooks.models import CallbackEvent

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Resolve missing attachment content types."

    def handle(self, *args, **options):
        """Resolve content types for all addAttachmentToCard events without one.
        """
        queryset = CallbackEvent.objects.filter(event_type='addAttachmentToCard')
        for event in queryset:
            if event.action_data.get('attachmentContentType'):
                continue
            content_type = event.resolve_attachment_content_type()
            if content_type:
                event.action_data['attachmentContentType'] = content_type
                event.save()
                logger.info(u'{url}: {content_type}'.format(
                    url=event.action_data['attachment']['url'],
                    content_type=content_type,
                ))
            else:
                logger.warning(u'{url}: could not resolve'.format(
                    url=event.action_data['attachment']['url'],
                ))
