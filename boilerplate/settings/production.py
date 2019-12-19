from .base import *

DEBUG = False

ALLOWED_HOSTS = ["ip-address", "www.myhost.com"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db-name",
        "USER": "db-username",
        "PASSWORD": "db-password",
        "HOST": "localhost",
        "PORT": ""
    }
}

