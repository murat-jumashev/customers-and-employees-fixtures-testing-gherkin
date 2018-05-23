from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from celery import shared_task


@shared_task
def send_email_async(mail_subject, message, to_email):
    import time
    time.sleep(5)
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

