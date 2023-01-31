from rest_framework import serializers
from .models import Company, Job
from superuser.models import CompanyCategory, CompanyDepartment
from superuser.serializers import CompanyCategorySerializer
from accounts.models import Account
from accounts.serializers import UserViewSerializer
from superuser.serializers import CompanyCategorySerializer


class CompanyProfileSerializerGet(serializers.ModelSerializer):
    recruiter = UserViewSerializer(read_only=True, many=False)
    category = CompanyCategorySerializer(read_only=True, many=False)
    class Meta:
        model = Company
        fields = '__all__'


class CompanyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_name', 'about', 'ceo_name', 'head_office_location', 'founder', 'company_logo']



class PostJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('created_at',)


class JobSerializerGet(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = '__all__'