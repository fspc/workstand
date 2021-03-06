import os
import sys
import rollbar

from .base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
WSGI_APPLICATION = 'bikeshop.wsgi.application'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secret')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['workstand.bikelover.org']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(message)s'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
        'bikeshop': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        }
    },
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': True,
        'BUNDLE_DIR_NAME': 'dist/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats-prod.json'),  # noqa
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

# Covers regular testing and django-coverage
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'  # noqa

MIDDLEWARE_CLASSES += ['rollbar.contrib.django.middleware.RollbarNotifierMiddleware']

ROLLBAR = {
    'access_token': '91808a727b9a4679a89720132071391a',
    'environment': 'production',
    'root': BASE_DIR,
}

rollbar.init(**ROLLBAR)

MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')
MAILCHIMP_USERNAME = 'drew@bcbc.bike'
