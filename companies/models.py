from django.db import models

from utils.timestamp import TimeStampModel


class Company(TimeStampModel):
    name    = models.CharField(max_length=15, unique=True)
    country = models.CharField(max_length=15)
    region  = models.CharField(max_length=15)

    class Meta:
        db_table = 'companies'