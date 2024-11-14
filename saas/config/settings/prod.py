import os
from .base import *  # noqa: F403
from dotenv import load_dotenv, find_dotenv
from google.oauth2 import service_account
from google.cloud import storage


load_dotenv(find_dotenv())

ALLOWED_HOSTS = ['more-django-857861010647.us-central1.run.app']

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

INSTALLED_APPS += [  # noqa: F405
                    
                ]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DEV_DB_NAME"),
        'HOST': os.getenv("DEV_DB_HOST"),
        'PASSWORD': os.getenv("DEV_DB_PASSWORD"),
        'USER': os.getenv("DEV_DB_USER"),
        'PORT': os.getenv("DEV_DB_PORT")
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
TO_EMAIL = os.getenv('TO_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_SSL = True