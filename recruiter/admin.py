from django.contrib import admin
from .models import  Company, Job, Qualification

# Register your models here.

# admin.site.register(RecruiterProfile)
admin.site.register(Company)
admin.site.register(Job)

class QulificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Qualification, QulificationAdmin)
