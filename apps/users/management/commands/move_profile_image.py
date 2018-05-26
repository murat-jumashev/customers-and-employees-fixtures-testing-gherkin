import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Copies profile.jpg to files/media/ folder"

    def handle(self, *args, **options):
        source = os.path.join(
            settings.BASE_DIR, 'apps', 'users', 'fixtures', 'profile.jpg')
        desitination = settings.MEDIA_ROOT
        shutil.copy(source, desitination)
        message = "{} файлын {} папкасына көчүрдүк".format(
            source, desitination)
        self.stdout.write(self.style.SUCCESS(message)) # pylint: disable=E1101
