from rest_framework import serializers
from .models import CompanyCategory, CompanyDepartment



class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = ['id', 'category_name']



class CategoryDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDepartment
        fields = ['id', 'department_name']
