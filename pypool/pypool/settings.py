# Django settings for wagtailtutorial project.

import os
from uuid import uuid4
import dj_database_url

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [x.strip() for x in os.environ.get('ADMIN_EMAILS', '').split(',')]
MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config('DATABASE_URL', 'sqlite:///{}'.format(os.path.join(PROJECT_ROOT,'dev.db')))
}

CONN_MAX_AGE = 600  # number of seconds database connections should persist for
ALLOWED_HOSTS = []
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_TZ = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'pypool', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = str(uuid4())

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'pypool.urls'
WSGI_APPLICATION = 'pypool.wsgi.application'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'pypool', 'templates'),
)

INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'compressor',
    'taggit',
    'modelcluster',
    'django.contrib.admin',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Auth settings
LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# WAGTAIL SETTINGS
WAGTAIL_SITE_NAME = 'pypool'

# Override the search results template for wagtailsearch
WAGTAILSEARCH_RESULTS_TEMPLATE = 'tutorial/search_results.html'
WAGTAILSEARCH_RESULTS_TEMPLATE_AJAX = 'tutorial/includes/search_listing.html'

WAGTAILSEARCH_ES_INDEX = 'pypool'