'''This is a standard django settings template

To use:

    django-admin.py startproject {{project_name}} --template=dbase/skeleton

Then go to {{project_name}}/project_settings and configure
all the files in there and the sub-directories.

Update {dev,prod,test}/_passwords.py appropriately.
Backup the _passwords.py files.
Soft-link appropriate directory to "local"

Then:

    cd <{{project_name}}>/
    pip install -r requirements.txt
    git init
    git add manage.py requirements.txt myproj
    cd <{{project_name}}>/{{project_name}}/
    git submodule add git@github.com:ngkabra/dutils.git
    git submodule add git@github.com:ngkabra/dbase.git

    create database {{project_name}}, user {{project_name}}
    python manage.py syncdb
'''

from project_settings.config import *
from os.path import join
import sys

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = join(PROJ_ROOT, 'site_media')
MEDIA_URL = '/site_media/'
ADMIN_MEDIA_PREFIX = '/static/admin/' # ?
# Except for localhost, these will be overridded by local/misc.py
STATIC_ROOT = join(PROJ_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)
TEMPLATE_LOADERS = (
    'dbtemplates.loader.Loader', # not to be cached...
    ('django.template.loaders.cached.Loader',
     ('django.template.loaders.filesystem.Loader',
      'django.template.loaders.app_directories.Loader',
      'django.template.loaders.eggs.Loader',
      )),
    )

MIDDLEWARE_CLASSES_PRE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',)

MIDDLEWARE_CLASSES_POST = (
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',)

ROOT_URLCONF = '{{project_name}}.urls'
TEMPLATE_DIRS = (join(PROJ_ROOT, 'templates'),)

CRISPY_TEMPLATE_PACK = 'bootstrap'

from project_settings.local._passwords import *
from project_settings.pipelines import *
from project_settings.local.database import *
try:
    from project_settings.local.logging import *
except ImportError:
    from project_settings.logging import *
from project_settings.local.misc import *
from project_settings.installed_apps import *
if 'test' in sys.argv:
    try:
        from project_settings.local.test import *
    except ImportError:
        pass

# must be set after importing _passwords
DATABASES['default']['PASSWORD'] = DATABASE_PASSWORD
RAVEN_CONFIG = {'dsn': RAVEN_DSN,}

if 'MANAGERS' not in locals():
    MANAGERS = ADMINS
if 'TEMPLATE_DEBUG' not in locals():
    TEMPLATE_DEBUG = DEBUG

if 'EXTRA_MIDDLEWARE' not in locals():
    EXTRA_MIDDLEWARE = ()
if 'DATABASE_ROUTERS' not in locals():
    DATABASE_ROUTERS = ()
if 'TEMPLATE_CONTEXT_PROCESSORS' not in locals():
    from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Remove disabled apps, and related middleware/context_processors
if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES_PRE = list(MIDDLEWARE_CLASSES_PRE)
    MIDDLEWARE_CLASSES_POST = list(MIDDLEWARE_CLASSES_POST)
    DATABASE_ROUTERS = list(DATABASE_ROUTERS)
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for a in DISABLED_APPS:
        for the_list in (MIDDLEWARE_CLASSES_PRE, MIDDLEWARE_CLASSES_POST,
                         DATABASE_ROUTERS, TEMPLATE_CONTEXT_PROCESSORS):
            for x, m in enumerate(the_list):
                if m.startswith(a):
                    the_list.pop(x)

# Add in extra apps/middleware/context_processors
if 'EXTRA_APPS' in locals():
    INSTALLED_APPS += EXTRA_APPS

MIDDLEWARE_CLASSES = (MIDDLEWARE_CLASSES_PRE +
                      list(EXTRA_MIDDLEWARE) +
                      MIDDLEWARE_CLASSES_POST)

if 'EXTRA_CONTEXT_PROCESSORS' in locals():
    TEMPLATE_CONTEXT_PROCESSORS += EXTRA_CONTEXT_PROCESSORS
