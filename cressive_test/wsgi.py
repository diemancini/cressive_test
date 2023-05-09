"""
WSGI config for cressive_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get("DJANGO_ENV")

if env in ["develop"]:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cressive_test.settings.develop")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cressive_test.settings.local")

application = get_wsgi_application()
