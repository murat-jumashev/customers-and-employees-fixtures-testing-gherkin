from django.db.models.signals import post_save
from django.contrib.auth.views import get_user_model
from django.contrib.auth.models import Group

from .models import Employee


def add_user_to_employees_group(sender, instance, created, **kwargs):
    if created:
        employees_group = Group.objects.get(name="Employees")
        employees_group.user_set.add(instance.user)
