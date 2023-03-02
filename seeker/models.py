from django.db import models
from accounts.models import Account
from superuser.models import Skill, CompanyCategory, CompanyDepartment
from recruiter.models import Company, Job
from notifications.models import Notifications

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime
from dateutil.relativedelta import relativedelta
# Create your models here.
from django.contrib.postgres.fields import ArrayField



class SeekerProfile(models.Model):

    SEEKER_STATUS = [
        ('fresher', 'fresher'),
        ('intermediate', 'intermediate'),
        ('professional', 'professional')
    ]
    seeker = models.ForeignKey(Account, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profle picture', blank=True)
    about = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True) 
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(CompanyDepartment, on_delete=models.CASCADE, blank=True, null=True)
    level = models.CharField(default='fresher', choices=SEEKER_STATUS, max_length=20)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    year_of_experience = models.PositiveIntegerField(null=True, blank=True, default=0)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.seeker)

@receiver(pre_save, sender=SeekerProfile)
def age_handler(sender, instance, **kwargs):
    if instance.date_of_birth:
        
        today = datetime.datetime.now()
        print(today)
        rdelta = relativedelta(today,instance.date_of_birth)
        instance.age = rdelta.years
        print(instance.age)
    


class Education(models.Model):

    user_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100, blank=True)
    branch_name = models.CharField(max_length=50, blank=True)

    college_name = models.CharField(max_length=100, blank=True)
    course_name = models.CharField(max_length=50, blank=True)

    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    description = models.TextField(blank=True)

    is_graduated = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)
    

    

class Experience(models.Model):
    user_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    is_current = models.BooleanField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField('/company_logo', blank=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return str(self.user_id)
    


class Projects(models.Model):
    user_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    is_current = models.BooleanField(default=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True)
    project_url = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.user_id)
    


class SeekerSkillSet(models.Model):
    user_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    skill_set_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_level = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.user_id)
    

class AppliedJobs(models.Model):

    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    recruiter_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    seeker_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resume')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    is_shortlisted = models.BooleanField(default=False)
    is_decline = models.BooleanField(default=False)
    is_applied = models.BooleanField(default=True)
    applied_on = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.job_id)
    
    def save(self,*args, **kwargs):
        if not self.is_shortlisted:
            user = self.recruiter_id.recruiter
            title = "New Job Application"
            notification = "You have new Application for your job post "+ self.job_id.job_title
            url = '/recruiter-single-job-view'
            parameter = self.job_id.id
            Notifications.objects.create(user=user, title = title, notification = notification, url=url, parameter=parameter)

        super(AppliedJobs, self).save(*args, **kwargs)
    

class FavouriteJob(models.Model):

    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    seeker_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.job_id)
    


class ReportJob(models.Model):
    seeker_id = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return str(self.job_id)
    
    def save(self,*args, **kwargs):
        if not self.pk:
            title = "Report On Job"
            notification = "A new report found on the job %s by %s company" % (self.job_id.job_title, self.job_id.company_id.company_name)
            url = '/job-management'
            Notifications.objects.create(is_admin=True, title = title, notification = notification, url=url)
            super(ReportJob, self).save(*args, **kwargs)
    
