from rest_framework import serializers
from .models import Company
from superuser.models import CompanyCategory
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
    # recruiter = UserViewSerializer(many=False)
    # category = CompanyCategorySerializer(many=True)

    class Meta:
        model = Company
        fields = ['company_name', 'about', 'ceo_name', 'head_office_location', 'founder', 'company_logo']

    # def update(self, instance, validated_data):
    #     recruiter_data = validated_data.pop('recruiter')
    #     category = validated_data.pop('category')
    #     category = CompanyCategory.objects.get(category_name = category.get('category_name'))
    #     company = instance
    #     company.company_name = validated_data.get('company_name')
    #     company.about = validated_data.get('about')
    #     company.ceo_name = validated_data.get('ceo_name')
    #     company.head_office_location = validated_data.get('head_office_location')
    #     company.founder = validated_data.get('founder')
    #     company.category = category
    #     company.save()
    #     user = company.recruiter
    #     user.first_name = recruiter_data.get('first_name')
    #     user.last_name = recruiter_data.get('last_name')
    #     user.email = recruiter_data.get('email', user.email)
    #     user.phone_number = recruiter_data.get('phone_number', user.phone_number)
    #     user.save()
    #     print(user.first_name)

    #     return company