from django.db import models
from accounts.models import Account
from notifications.models import Notifications

# Create your models here.

class AdminProfile(models.Model):
    admin = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class CompanyCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class CompanyDepartment(models.Model):
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name


class Skill(models.Model):
    department = models.ForeignKey(CompanyDepartment, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name
    


class PaymentDetails(models.Model):
    user = models.ForeignKey('recruiter.company', on_delete = models.DO_NOTHING)
    membership = models.ForeignKey('recruiter.SubscriptionPlan', on_delete=models.DO_NOTHING)
    amount_paid = models.FloatField(max_length=10)
    payment_id = models.CharField(max_length=100, null=True)
    payment_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.amount_paid)
    
    def save(self,*args, **kwargs):
        if not self.pk:
            user = self.user.recruiter
            title = "Plan purchase Successfull"
            notification = "Successfully subscribed for the "+ self.membership.membership.title+ " plan. Your Plan's validiy is "+ str(self.membership.membership.duration) + ' days'
            Notifications.objects.create(user=user, title = title, notification = notification)
            title = "New Subsciption Found"
            notification = "%s company upgraded %s plan" % (self.user.company_name, self.membership.membership.title)
            Notifications.objects.create(is_admin=True, title = title, notification = notification)

            super(PaymentDetails, self).save(*args, **kwargs)



