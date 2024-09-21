from .base import *

ALLOWED_HOST = []

INSTALLED_APPS += ["users"]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        'NAME': 'local_db',
        'HOST': '127.0.0.1',
        'PASSWORD': 'testing321',
        'USER': 'django_local_user',
        'PORT': '5432'
    }
}
