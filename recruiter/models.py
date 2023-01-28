from django.db import models
from accounts.models import Account
from superuser.models import CompanyCategory, CompanyDepartment

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    recruiter = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    employer_id = models.CharField(max_length=50, unique=True, blank=True, null=True, default=1)
    category = models.ForeignKey(CompanyCategory, on_delete=models.PROTECT)
    company_logo = models.ImageField(upload_to=f'media/{company_name}/logo', blank=True)
    started_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    about = models.TextField(max_length=3000, blank=True)
    founder = models.CharField(max_length=200, blank=True)
    ceo_name = models.CharField(max_length=200, blank=True)
    head_office_location = models.CharField(max_length=100)


    def __str___(self):
        return self.id



# class RecruiterProfile(models.Model):
#     recruiter = models.ForeignKey(Account, on_delete=models.CASCADE)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     profile_pic = models.ImageField('/images', blank=True)
#     about = models.TextField(blank=True)
#     category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, blank=True, null=True)


#     def __str__(self):
#         return str(self.id)


class Qualification(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Job(models.Model):

    SALARY_TYPE = [
        ()
    ]
