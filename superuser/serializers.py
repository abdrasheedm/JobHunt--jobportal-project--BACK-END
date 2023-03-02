from rest_framework import serializers
from .models import CompanyCategory, CompanyDepartment, PaymentDetails
from accounts.models import Account
from accounts.serializers import UserTypeSerializer
from notifications.models import Notifications
from recruiter.models import Qualification, SubscriptionPlan


class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = '__all__'



class CategoryDepartmentSerializer(serializers.ModelSerializer):
    category = CompanyCategorySerializer(read_only=True)
    class Meta:
        model = CompanyDepartment
        fields = ['id', 'department_name', 'category']


class CategoryDepartmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDepartment
        fields = '__all__'


class AlluserViewSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer(read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'user_type', 'is_active']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['title', 'notification', 'created_at', 'url', 'parameter']


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'



class PaymentDetailSerializer(serializers.ModelSerializer):

    from recruiter.serilaizers import CompanyProfileSerializerGet
    from recruiter.serilaizers import SubsciptionPlanGetSerializer

    user = CompanyProfileSerializerGet(read_only=True)
    membership = SubsciptionPlanGetSerializer(read_only=True)

    class Meta:
        model = PaymentDetails
        fields = '__all__'