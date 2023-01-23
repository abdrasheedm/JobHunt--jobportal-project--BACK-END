from django.db import models
from accounts.models import Account

# Create your models here.


class CompanyProfile(models.Model):
    recruiter = models.ForeignKey(Account, on_delete=models.CASCADE)
