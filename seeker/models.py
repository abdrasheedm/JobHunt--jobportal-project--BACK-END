from django.db import models
from accounts.models import Account
from superuser.models import Skill, CompanyCategory, CompanyDepartment

# Create your models here.


class SeekerProfile(models.Model):

    SEEKER_STATUS = [
        ('fresher', 'fresher'),
        ('intermediate', 'intermediate'),
        ('professional', 'professional')
    ]
    seeker = models.ForeignKey(Account, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)
    profile_photo = models.ImageField('/images/', blank=True)
    about = models.TextField(blank=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(CompanyDepartment, on_delete=models.CASCADE, blank=True, null=True)
    level = models.CharField(default='fresher', choices=SEEKER_STATUS, max_length=20)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    Country = models.CharField(max_length=20, blank=True)
    # education = 
    # experience = 
    # website = 
    # projects = 

    def __str__(self):
        return ""
