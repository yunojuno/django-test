# -*- coding: utf-8 -*-
from settings import *  # noqa

HIPCHAT_ENABLED = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

# the django apps aren't required for the tests,
INSTALLED_APPS = (
    'trello_webhooks', 'test_app'
)

