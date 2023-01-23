from django.db import models
from accounts.models import Account

# Create your models here.

class AdminProfile(models.Model):
    admin = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
