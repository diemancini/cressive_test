import os
from cressive_test.settings.common import *
from cressive_test.settings.common import BASE_DIR


# Configure default domain name
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

CRESSIVE_TEST_URL = os.getenv("CRESSIVE_TEST_URL")
DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, DATABASE_NAME),
    }
}

SHOW_PASSWORD_LOGIN = True

CRONJOBS = [
    ('0 0 * * *', 'scraping.cron.start_scraping', '>> /cron/django_cron.log')
]
CRONTAB_COMMAND_SUFFIX = '2>&1'