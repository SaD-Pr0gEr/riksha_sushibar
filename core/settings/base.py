import logging.config
import os
from pathlib import Path

from django.utils.log import DEFAULT_LOGGING
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.users.apps.UsersConfig',
    'apps.products.apps.ProductsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING_CONFIG = None
LOGLEVEL = os.getenv('LOGLEVEL', 'INFO').upper()
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'app': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        }
    },
})

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
PHOTOS_DIR = 'photos'
PHOTOS_FULL_DIR_PATH = MEDIA_ROOT / PHOTOS_DIR
PRODUCT_PHOTO_DIR = '/'.join([PHOTOS_DIR, 'product'])
PRODUCT_PHOTO_FULL_DIR_PATH = MEDIA_ROOT / PRODUCT_PHOTO_DIR

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ICON_FORMATS = ['.svg']

AUTH_USER_MODEL = 'users.User'
