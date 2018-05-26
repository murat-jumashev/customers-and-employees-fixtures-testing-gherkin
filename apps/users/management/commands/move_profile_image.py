import os
import shutil
from django.conf import settings
from django.core.management import BaseCommand

DESTINATION = settings.MEDIA_ROOT

def create_files_dir():
    if not os.path.exists(DESTINATION):
        os.makedirs(DESTINATION)

class Command(BaseCommand):
    help = "Command to copy profile.jpg to files/media"

    def handle(self, *args, **kwargs):
        source = os.path.join(
            settings.BASE_DIR, 'apps', 'users', 'fixtures', 'profile.jpg')
        create_files_dir()
        shutil.copy(source, DESTINATION)
        message = "{} файлын {} папкасына көчүрдүк".format(source, DESTINATION)
        self.stdout.write(self.style.SUCCESS(message)) # pylint: disable=E1101
