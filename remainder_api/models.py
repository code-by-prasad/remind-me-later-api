from random import choice

from django.db import models

# Create your models here.
class Remainder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=100)
    class RemindVia(models.TextChoices):
        EMAIL = 'email', 'Email'
        SMS = 'sms', 'Sms'

    remind_via = models.CharField(max_length=10, choices=RemindVia.choices)
