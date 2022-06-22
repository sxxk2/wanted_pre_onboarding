from django.db import models

from utils.timestamp import TimeStampModel


class User(TimeStampModel):
    email  = models.EmailField(max_length=50, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    name   = models.CharField(max_length=20)

    class Meta:
        db_table = "users"