import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

# app = Celery('store', broker_url='redis://redis:6379/0')  # for docker
app = Celery('store', broker_url='redis://127.0.0.1:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
