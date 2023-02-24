from rest_framework import serializers
from .models import CompanyCategory, CompanyDepartment
from accounts.models import Account
from accounts.serializers import UserTypeSerializer



class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = ['id', 'category_name']



class CategoryDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDepartment
        fields = ['id', 'department_name']


class AlluserViewSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_type', 'is_active']
