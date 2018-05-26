import os
from django.conf import settings
from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_save


PROFILE_IMAGE_IN_MEDIA = os.path.join(settings.MEDIA_ROOT, 'profile.jpg')


class UsersConfig(AppConfig):
    name = 'apps.users'

    def ready(self):
        from .models import Employee
        from .signals import add_user_to_employees_group
        post_save.connect(add_user_to_employees_group, sender=Employee)
        if not os.path.exists(PROFILE_IMAGE_IN_MEDIA):
            call_command('move_profile_image')
