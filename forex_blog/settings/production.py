from .base import *

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ["139.162.226.107", "www.forexquantfx.com", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": "",
    }
}

