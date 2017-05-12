# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trello_webhooks', '0002_webhook_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackevent',
            name='event_payload',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='callbackevent',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
