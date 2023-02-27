from django.db import models
from accounts.models import Account
from notifications.models import Notifications
from superuser.models import CompanyCategory, CompanyDepartment
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime
import time



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
    

    def save(self,*args, **kwargs):
        if not self.pk:
            title = "New Job Post !"
            notification = ("A new job is posted by the company %s on title %s" % (self.company_id.company_name, self.job_title))
            Notifications.objects.create(is_admin=True, title = title, notification = notification)
            print('created notificaion')

            super(Job, self).save(*args, **kwargs)
    


class ShortlistedCandidates(models.Model):
    STATUS = [
        ('Shortlised' , 'Shortlised'),
        ('Tech-Interview' ,'Tech-Interview'),
        ('HR-Round','HR-Round')
    ]
    recruiter_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    applied_job = models.ForeignKey('seeker.AppliedJobs', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(default = 'Shortlised' ,choices=STATUS , max_length=200 ,blank=True ) 

    def __str__(self):
        return str(self.applied_job)

    def save(self,*args, **kwargs):
        if not self.pk:
            user = self.applied_job.seeker_id.seeker
            title = "Shortlisted !"
            notification = ("Congratulations you have been shortlisted for the job %s by posted by the company %s" % (self.applied_job.job_id.job_title, self.recruiter_id.company_name))
            Notifications.objects.create(user=user, title = title, notification = notification)

            super(ShortlistedCandidates, self).save(*args, **kwargs)
    



    


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
    job_count = models.PositiveBigIntegerField(default=5)

    def __str__(self):
        return self.title
    

class MembershipPurchase(models.Model):


    user = models.OneToOneField(Company, on_delete=models.CASCADE)
    membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    postable_job_count = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_active_job = models.BooleanField(default=True)
    activation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

@receiver(pre_save, sender=MembershipPurchase)
def job_count_handler(sender, instance, **kwargs):
    from django.utils import timezone
    if instance.expiry_date:
        if instance.expiry_date < timezone.now().date():
            instance.is_active = False
    if instance.is_active_job==True and instance.postable_job_count==0:
        instance.postable_job_count = instance.membership.job_count


@receiver(post_save, sender=MembershipPurchase)
def expirty_date_handler(sender, instance, **kwargs):
    print('hai')
    if instance.activation_date and not instance.expiry_date:
        duration = instance.membership.duration
        activation_date = instance.activation_date
        expiry_date = activation_date + datetime.timedelta(days=duration)
        instance.expiry_date = expiry_date
        instance.save()
    

class SubscriptionPlan(models.Model):
    user = models.ForeignKey(Company, on_delete=models.CASCADE)
    membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE, null=True)
    activation_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=SubscriptionPlan)
def expirty_date_handler(sender, instance, **kwargs):
    print('hai')
    if instance.activation_date and not instance.expiry_date:
        duration = instance.membership.duration
        activation_date = instance.activation_date
        expiry_date = activation_date + datetime.timedelta(days=duration)
        instance.expiry_date = expiry_date
        instance.save()
    





