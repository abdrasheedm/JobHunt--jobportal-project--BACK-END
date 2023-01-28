from django.contrib import admin
from .models import AdminProfile, CompanyCategory, CompanyDepartment

# Register your models here.

admin.site.register(AdminProfile)
admin.site.register(CompanyCategory)
admin.site.register(CompanyDepartment)