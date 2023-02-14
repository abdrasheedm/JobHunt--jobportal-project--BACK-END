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
    started_date = models.DateField(auto_now_add=True, blank=True, null=True)
    about = models.TextField(max_length=3000, blank=True)
    founder = models.CharField(max_length=200, blank=True)
    ceo_name = models.CharField(max_length=200, blank=True)
    head_office_location = models.CharField(max_length=100)


    def __str__(self):
        return self.company_name


class Qualification(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Job(models.Model):

    JOB_TYPE = [
        ('part-time', 'Part Time'),
        ('full-time', 'Full Time'),
        ('intern', 'Intern'),
    ]

    LEVEL = [
        ('fresher', 'Fresher'),
        ('internship', 'Internship'),
        ('intermediate', 'Intermediate'),
        ('professional', 'Professional')
    ]


    job_title = models.CharField(max_length=200)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    recruiter_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    department = models.ForeignKey(CompanyDepartment, on_delete=models.CASCADE)
    level = models.CharField(default='fresher', choices=LEVEL, max_length=200, blank=True)
    experience = models.IntegerField(blank=True, null=True)
    salary_range = models.CharField(max_length=20, blank=True, null=True)
    job_type = models.CharField(default='full-time', choices=JOB_TYPE, max_length=200, blank=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, blank=True)
    full_description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    vacancy = models.PositiveIntegerField(blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.job_title
    


class UserMembership(models.Model):
    DURATION = (
        (0, '15 days'),
        (30 , 'One Month'),
        (90 , 'Three Month'),
        (180 , 'Six Month'),
    )
    title = models.CharField(max_length=200 , default='Trial')
    duration = models.IntegerField(default=15 , choices=DURATION)
    price = models.CharField(max_length=200, default=0.00)

    def __str__(self):
        return self.title
    

class MembershipPurchase(models.Model):
    user = models.ForeignKey(Company, on_delete=models.CASCADE)
    membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    

class SubscriptionPlan(models.Model):
    user = models.ForeignKey(MembershipPurchase, on_delete=models.CASCADE)
    activation_date = models.DateField(auto_now_add=True)
    expirty_date = models.DateField()
    payment_id = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    paid = models.BooleanField(default=True)


    def __str__(self):
        return self.user