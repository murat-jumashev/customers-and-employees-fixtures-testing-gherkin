import os
from celery import Celery
from django.apps import apps, AppConfig


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('customers_and_employees')


class CeleryConfig(AppConfig):
    name = 'apps.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        app.config_from_object('django.conf:settings', namespace='CELERY')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print('Request {0!r}'.format(self.request))
