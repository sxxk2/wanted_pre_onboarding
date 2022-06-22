from django.db import models

from utils.timestamp  import TimeStampModel
from companies.models import Company
from users.models     import User

class Recruiting(TimeStampModel):
    company    = models.ForeignKey("companies.Company", on_delete=models.CASCADE)
    position   = models.CharField(max_length=20)
    reward     = models.IntegerField()
    content    = models.TextField()
    tech_stack = models.CharField(max_length=20)

    class Meta:
        db_table = 'recruitings'


class Application(TimeStampModel):
    recruiting = models.ForeignKey(Recruiting, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "applications"