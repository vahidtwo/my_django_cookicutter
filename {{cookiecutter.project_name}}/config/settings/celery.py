from config.env import env

# https://docs.celeryproject.org/en/stable/userguide/configuration.html


CELERY_TIMEZONE = "fa_IR"

CELERY_BROKER_URL = f"redis://{env('REDIS_HOST')}/2"
CELERY_RESULT_BACKEND = f"redis://{env('REDIS_HOST')}"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_BEAT_SCHEDULE = {
    # "calculate_due_date": {
    #     "task": "apps.infra.tasks.calculate_due_date",
    #     "schedule": crontab(hour=2),
    # }
}
