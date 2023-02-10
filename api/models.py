from django.db import models

# Create your models here.


class Me(models.Model):
    name = models.CharField(max_length=20)

class You(models.Model):
    me = models.ForeignKey(Me, on_delete=models.CASCADE)
    you = models.CharField(max_length=200)


