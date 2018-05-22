from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from .models import Employee
        from .signals import add_user_to_employees_group
        post_save.connect(add_user_to_employees_group, sender=Employee)
