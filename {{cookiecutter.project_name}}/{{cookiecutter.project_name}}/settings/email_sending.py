from {{cookiecutter.project_slug}}.setting.env import env, env_to_enum


# local | mailtrap
EMAIL_SENDING_STRATEGY =  env("EMAIL_SENDING_STRATEGY", default="local")


EMAIL_SENDING_FAILURE_TRIGGER = env.bool("EMAIL_SENDING_FAILURE_TRIGGER", default=False)
EMAIL_SENDING_FAILURE_RATE = env.float("EMAIL_SENDING_FAILURE_RATE", default=0.2)

if EMAIL_SENDING_STRATEGY == 'local':
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = env("EMAIL_PORT")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS")
    SERVER_EMAIL = "noreply@bernetco.ir"
