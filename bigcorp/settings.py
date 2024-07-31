from datetime import timedelta
from pathlib import Path

import environ
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(ENV_DIR / ".env")

SECRET_KEY = "django-insecure-gtoys4#d-)04r0$bnvo%27(es0sp%50$n*3nxg*wp*9!rz0t8t"

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party libraries
    "mathfilters",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_email_verification",
    "sorl.thumbnail",
    "django_celery_beat",
    "django_celery_results",
    "django_htmx",
    "rest_framework",
    "djoser",
    "drf_yasg",
    # apps
    "shop.apps.ShopConfig",
    "cart.apps.CartConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bigcorp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "bigcorp" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Custom Context Processors
                "shop.context_processors.categories",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "bigcorp.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env("POSTGRES_DB"),
#         "USER": env("POSTGRES_USER"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "HOST": env("POSTGRES_HOST"),
#         "PORT": env("POSTGRES_PORT", default=5432),
#     }
# }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Project Inside settings
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True
APPEND_SLASH = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "bigcorp" / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}
