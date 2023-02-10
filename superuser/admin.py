from django.contrib import admin
from .models import AdminProfile, CompanyCategory, CompanyDepartment, Skill

# Register your models here.

admin.site.register(AdminProfile)

class CompanyCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

admin.site.register(CompanyCategory, CompanyCategoryAdmin)

class CompanyDepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_name', 'category')
    list_display_links = ('department_name',)
admin.site.register(CompanyDepartment, CompanyDepartmentAdmin)
admin.site.register(Skill)
