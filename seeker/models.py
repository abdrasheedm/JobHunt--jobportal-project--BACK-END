from django.db import models
from accounts.models import Account

# Create your models here.


class SeekerProfile(models.Model):
    seeker = models.ForeignKey(Account, on_delete=models.CASCADE)
