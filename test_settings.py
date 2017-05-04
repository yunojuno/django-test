# -*- coding: utf-8 -*-
import dj_database_url

SECRET_KEY = "tests"

ROOT_URLCONF = 'test_app.urls'

DATABASES = {
    # automatically assumes DATABASE_URL env var
    'default': dj_database_url.config()
}

# the django apps aren't required for the tests,
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'trello_webhooks',
    'test_app'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
CALLBACK_DOMAIN = ''
HIPCHAT_API_TOKEN = ''
HIPCHAT_ROOM_ID = ''
HIPCHAT_ENABLED = False
