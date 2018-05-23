from threading import Thread
from django.shortcuts import render
from django.core.mail import EmailMessage


class EmailThread(Thread):
    def __init__(self, myemail):
        self.myemail = myemail
        Thread.__init__(self)

    def run(self):
        print('====started in a new thread====')
        import time; time.sleep(5)
        self.myemail.send()
        print('====message sent in a new thread====')


class EmailMessageInThread(EmailMessage):
    def send_async(self, fail_silently=False):
        thread = EmailThread(self)
        thread.start()
