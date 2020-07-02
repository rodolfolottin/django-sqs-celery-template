import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")

CELERY_CONFIG = {
    "CELERY_TASK_SERIALIZER": "json",
    "CELERY_ACCEPT_CONTENT": ["json"],
    "CELERY_RESULT_SERIALIZER": "json",
    "CELERY_RESULT_BACKEND": None,
    "CELERY_TIMEZONE": "America/Sao_Paulo",
    "CELERY_ENABLE_UTC": True,
    "CELERY_ENABLE_REMOTE_CONTROL": False,
}


CELERY_CONFIG.update(
    **{
        "BROKER_URL": settings.BROKER_URL,
        "BROKER_TRANSPORT": "sqs",
        "BROKER_TRANSPORT_OPTIONS": {
            "region": settings.SQS_REGION,
            "visibility_timeout": 3600,
            "polling_interval": 60,
        },
    }
)


app.conf.update(**CELERY_CONFIG)
app.autodiscover_tasks(packages={"payment.tasks"})
