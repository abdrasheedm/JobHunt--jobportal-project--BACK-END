from rest_framework import serializers
from .models import Company, Job, Qualification, MembershipPurchase, SubscriptionPlan, UserMembership, ShortlistedCandidates
from superuser.models import CompanyCategory, CompanyDepartment
from superuser.serializers import CompanyCategorySerializer
from accounts.models import Account
from accounts.serializers import UserViewSerializer
from superuser.serializers import CompanyCategorySerializer, CategoryDepartmentSerializer
# from seeker.serializers import AppliedJobsGetSerializer
# from seeker.serializers import AppliedJobsGetSerializer


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



class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = '__all__'



class PostJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('created_at',)


class JobSerializerGet(serializers.ModelSerializer):

    category = CompanyCategorySerializer(read_only = True, many=False)
    company_id = CompanyProfileSerializerGet(read_only=True, many=False)
    department = CategoryDepartmentSerializer(read_only=True, many=False)
    qualification = QualificationSerializer(read_only = True, many = False)
    
    class Meta:
        model = Job
        fields = '__all__'




class UserMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembership
        fields = '__all__'




class SubsciptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['user', 'membership']
        read_only_fields = ('activation_date', 'expiry_date', 'is_active')





class MembershipPurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipPurchase
        fields = '__all__'



class MembershipPurchaseGetSerializer(serializers.ModelSerializer):
    membership = UserMembershipSerializer(read_only=True, many=False)
    class Meta:
        model = MembershipPurchase
        fields = '__all__'




class SubsciptionPlanGetSerializer(serializers.ModelSerializer):
    membership = UserMembershipSerializer(read_only=True, many=False)
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'


class ShortlistCandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortlistedCandidates
        fields = '__all__'
