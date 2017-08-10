from __future__ import absolute_import, unicode_literals

import os
from .base import *  # noqa: F403, F401

try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass

DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')

# Domain specific
#
BASE_URL = os.environ.get('DJANGO_BASE_URL', 'https://example.com')
STATIC_URL = os.environ.get('DJANGO_STATIC_URL', '/static/')
MEDIA_URL = os.environ.get('DJANGO_MEDIA_URL', '/media/')

# Database settings
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DJANGO_DB_NAME'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
        'HOST': os.environ['DJANGO_DB_HOST'],
        'PORT': os.environ['DJANGO_DB_PORT'],
        'CONN_MAX_AGE': os.environ.get('DJANGO_DB_MAX_AGE', 600)
    }
}

# Static and media files
#
STATIC_ROOT = os.environ['DJANGO_STATIC_ROOT']
MEDIA_ROOT = os.environ['DJANGO_MEDIA_ROOT']

# Optional Elasticsearch backend - disabled by default
#
try:
    es_host = os.environ.get('DJANGO_ES_HOST', 'disable')

    if es_host == 'disable':
        WAGTAILSEARCH_BACKENDS = {}
    else:
        WAGTAILSEARCH_BACKENDS = {
            'default': {
                'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch2',
                'URLS': [es_host],
                'INDEX': 'wagtail',
                'TIMEOUT': 5,
                'OPTIONS': {
                    'ca_certs': os.environ['DJANGO_ES_CA_PATH'],
                    'use_ssl': True,
                }
            }
        }
except KeyError:
    pass
