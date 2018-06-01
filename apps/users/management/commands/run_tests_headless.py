import os
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        os.environ[settings.TEST_MODE] = settings.HEADLESS
        call_command('behave', '--use-existing-database')
