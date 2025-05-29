"""
WSGI config for saas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv, find_dotenv
from django.core.wsgi import get_wsgi_application  # noqa: E402

load_dotenv(find_dotenv())

ENV = os.getenv('ENV')

if ENV == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
application = get_wsgi_application()
