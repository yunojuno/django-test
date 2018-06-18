# -*- coding: utf-8 -*-
from os import environ, path

import dj_database_url

from django.core.exceptions import ImproperlyConfigured

# ============= APP SETTINGS =====================
MANDATORY_ENVIRONMENT_SETTINGS = (
    'TRELLO_API_KEY',
    'TRELLO_API_SECRET',
    'CALLBACK_DOMAIN',
    'DATABASE_URL'
)
for s in MANDATORY_ENVIRONMENT_SETTINGS:
    if s not in environ:
        raise ImproperlyConfigured(u"Missing environment variable: '%s'" % s)
# ------------------------------------------------
TRELLO_API_KEY = environ['TRELLO_API_KEY']
TRELLO_API_SECRET = environ['TRELLO_API_SECRET']
CALLBACK_DOMAIN = environ['CALLBACK_DOMAIN']
# optional for the test app to send updates to HipChat
HIPCHAT_API_TOKEN = environ.get('HIPCHAT_API_TOKEN', None)
HIPCHAT_ROOM_ID = environ.get('HIPCHAT_ROOM_ID', None)
HIPCHAT_ENABLED = HIPCHAT_API_TOKEN and HIPCHAT_ROOM_ID
if HIPCHAT_ENABLED:
    print u"HipChat integration is ENABLED: %s" % HIPCHAT_ROOM_ID
else:
    print u"HipChat integration is DISABLED"
# ============= / APP SETTINGS ===================

DEBUG = environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

# You should really update this in your app!
# see https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '*')

USE_L10N = True
USE_I18N = True
USE_TZ = True
TIMEZONE = 'Europe/London'

DATABASES = {
    # automatically assumes DATABASE_URL env var
    'default': dj_database_url.config()
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_app',
    'trello_webhooks',
)

MIDDLEWARE_CLASSES = [
    # default django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_DIRS = (
)

PROJECT_ROOT = path.realpath(path.dirname(__file__))
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

SECRET_KEY = "secret"

# requests can be really noisy, and it uses a bunch of different
# loggers, so use this to turn all requests-related loggers down
REQUESTS_LOGGING_LEVEL = environ.get('REQUESTS_LOGGING_LEVEL', 'WARNING')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'trello_webhooks': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'requests': {
            'handlers': ['console'],
            'level': REQUESTS_LOGGING_LEVEL,
            'propagate': False,
        },
        'urllib3': {
            'handlers': ['console'],
            'level': REQUESTS_LOGGING_LEVEL,
            'propagate': False,
        },
        'oauthlib': {
            'handlers': ['console'],
            'level': REQUESTS_LOGGING_LEVEL,
            'propagate': False,
        },
        'requests_oauthlib': {
            'handlers': ['console'],
            'level': REQUESTS_LOGGING_LEVEL,
            'propagate': False,
        },
    }
}

ROOT_URLCONF = 'test_app.urls'

APPEND_SLASH = True


# set HOSTED_ON_AWS environ var to any value
# along with access keys etc. in order to use S3 storage 
# if hosted on AWS.
# You will also need the following requirements:
# boto3==1.7.40
# django-storages==1.6.6
HOSTED_ON_AWS = environ.get('HOSTED_ON_AWS', False)

if HOSTED_ON_AWS:
    AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'static'

    STATICFILES_DIRS = [
        path.join(BASE_DIR, 'test_app/static'),
    ]
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_LOCATION = 'static'

else:
    STATIC_URL = "/static/"
    STATIC_ROOT = path.join(PROJECT_ROOT, 'static')

