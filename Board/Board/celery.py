import os
from celery import Celery
from celery.schedules import crontab
from NoticeBoard.tasks import delete_old_codes
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Board.settings')
 
app = Celery('Board')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.beat_schedule = {
    'every minute': {
        'task': delete_old_codes,
        'schedule': crontab(),
    }
}

app.autodiscover_tasks()