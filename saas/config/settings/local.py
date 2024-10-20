import os
from .base import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ALLOWED_HOST = []

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

INSTALLED_APPS += [
                    "users",
                    "products",
                    "orders",
                    "rest_framework_simplejwt"
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
