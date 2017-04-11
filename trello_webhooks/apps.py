from __future__ import unicode_literals

from django.apps import AppConfig


class TrelloWebhooksConfig(AppConfig):
    name = 'trellowebhooks'
    verbose_name = "Trello Webhooks"

    def ready(self):
        import jsonfield_compat
        jsonfield_compat.register_app(self)
