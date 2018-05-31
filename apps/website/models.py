from django.db import models


class ContactMessage(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "Message from {} {}".format(self.name, self.email)
