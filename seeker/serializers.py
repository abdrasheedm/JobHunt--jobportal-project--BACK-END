from rest_framework import serializers
from accounts.serializers import UserViewSerializer
from superuser.serializers import CompanyCategorySerializer, CategoryDepartmentSerializer
from .models import SeekerProfile, Education, Experience, SeekerSkillSet, Projects, AppliedJobs, FavouriteJob, ReportJob, ReportJob
from recruiter.serilaizers import JobSerializerGet, ShortlistedCandidates




class SeekerProfileSerializer(serializers.ModelSerializer):

    seeker = UserViewSerializer(read_only=True, many=False)
    category = CompanyCategorySerializer(read_only=True, many=False)
    department = CategoryDepartmentSerializer(read_only=True, many=False)
    class Meta:
        model = SeekerProfile
        fields = '__all__'



class SeekerProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = '__all__'


class EducationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = '__all__' 


class AppliedJobsGetSerializer(serializers.ModelSerializer):
    job_id = JobSerializerGet(read_only=True, many=False)
    seeker_id = SeekerProfileSerializer(read_only=True, many=False)
    class Meta:
        
        model = AppliedJobs
        fields = '__all__'



class FavouriteJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteJob
        fields = '__all__'


class FavouriteJobGetSerializer(serializers.ModelSerializer):
    job_id = JobSerializerGet(read_only=True, many=False)
    class Meta:
        model = FavouriteJob
        fields = ['id', 'job_id']



class ShortlistCandidatesGetSerializer(serializers.ModelSerializer):
    applied_job = AppliedJobsGetSerializer(read_only=True, many=False)
    class Meta:
        model = ShortlistedCandidates
        fields = '__all__'


class ReportJobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportJob
        fields = '__all__'

    
class RepsortJobGetSerializer(serializers.ModelSerializer):
    job_id = JobSerializerGet(read_only=True)
    seeker_id = SeekerProfileSerializer(read_only=True)
    class Meta:
        model = ReportJob
        fields = '__all__'





        