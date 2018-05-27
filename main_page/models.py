from django.db import models

from datetime import datetime

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    msg = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now)
    sent = models.BooleanField(default=False)
