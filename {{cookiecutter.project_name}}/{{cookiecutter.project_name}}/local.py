from {{cookiecutter.project_name}}.base import *  # noqa

PYPI_MODULES = [
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_generators",
    "django_filters",
    "corsheaders",
    "drf_yasg",
]
INTERNAL_IPS = [
    "127.0.0.1",
]
INSTALLED_APPS = [
    "debug_toolbar",
    *LIB_MODULES,
    *DJANGO_APP,
    *PYPI_MODULES,
    *APP_MODULES,
]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware", *MIDDLEWARE]
ADMINS = [("{{cookiecutter.first_name}}", "{{cookiecutter.email}}")]
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {"format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"},
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"},
        "mail_admins": {"level": "ERROR", "class": "django.utils.log.AdminEmailHandler"},
    },
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "django": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False,
        },
        "django.request": {
            "handlers": ["mail_admins", "console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
