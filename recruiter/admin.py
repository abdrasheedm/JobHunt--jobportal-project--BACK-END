from django.contrib import admin
from .models import  Company, Job, Qualification, MembershipPurchase, SubscriptionPlan, UserMembership

# Register your models here.

# admin.site.register(RecruiterProfile)
admin.site.register(Company)

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'category', 'department')
admin.site.register(Job, JobAdmin)

class QulificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Qualification, QulificationAdmin)
admin.site.register(MembershipPurchase)
admin.site.register(SubscriptionPlan)
admin.site.register(UserMembership)

