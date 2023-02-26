from rest_framework import serializers
from .models import CompanyCategory, CompanyDepartment
from accounts.models import Account
from accounts.serializers import UserTypeSerializer



class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = '__all__'



class CategoryDepartmentSerializer(serializers.ModelSerializer):
    category = CompanyCategorySerializer(read_only=True)
    class Meta:
        model = CompanyDepartment
        fields = ['id', 'department_name', 'category']


class AlluserViewSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_type', 'is_active']
