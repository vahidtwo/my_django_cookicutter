from {{cookiecutter.project_name}}.base import *  # noqa
# Based on https://www.hacksoft.io/blog/optimize-django-build-to-run-faster-on-github-actions

DEBUG = False
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
PYPI_MODULES = [
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "drf_yasg",
]
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        }
    }
INSTALLED_APPS = [*DJANGO_APP, *PYPI_MODULES, *APP_MODULES, *LIB_MODULES]
ELASTIC_APM_DISABLE_SEND = True
CELERY_BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True