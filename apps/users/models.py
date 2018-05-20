from django.db import models
from django.conf import settings
from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    full_name = models.CharField('full name', max_length=255, blank=True)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return '<{}>'.format(self.email)


def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)


class Customer(models.Model):
    default_profile_image = 'profile.jpg'
    photo = models.ImageField(
        default=default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer'
    )
    class Meta:
        permissions = [
            ('can_view','Can view customers')
        ]

    
    def __str__(self):
        return "{} customer profile".format(self.user.email) #pylint: disable=E1101


def resume_upload_to(instance, filename):
    return 'resumes/{0}/{1}'.format(instance.user.pk, filename)


class Employee(models.Model):
    resume = models.FileField(
        upload_to=resume_upload_to,
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee'
    )
    class Meta:
        permissions = [
            ('can_view','Can view employees')
        ]

    def __str__(self):
        return "{} employee profile".format(self.user.email) #pylint: disable=E1101
