from datetime import datetime
from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.


class User(models.Model):
    phone = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=20)
    ivr_code = models.CharField(max_length=10)
    token = models.CharField(max_length=200)
    identifier = models.CharField(primary_key=True, max_length=100)

    notify_morning = models.BooleanField(default=True)
    notify_noon = models.BooleanField(default=True)

    def __str__(self):
        return self.last_name


class Test(models.Model):
    user = models.ForeignKey(
        User, to_field="identifier", on_delete=models.CASCADE, default=None
    )

    date_checked = models.DateField()
    testing = models.BooleanField(default=False)
    message = models.CharField(max_length=200, default="")
