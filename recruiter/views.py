from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Company, Job, Qualification, MembershipPurchase, UserMembership, SubscriptionPlan, ShortlistedCandidates
from superuser.models import CompanyCategory, CompanyDepartment
from superuser.serializers import CompanyCategorySerializer
from accounts.models import Account
from .serilaizers import (CompanyProfileSerializerGet, CompanyProfileSerializer, PostJobSerializer,  JobSerializerGet, QualificationSerializer, SubsciptionPlanSerializer, 
                          MembershipPurchaseSerializer, UserMembershipSerializer, SubsciptionPlanGetSerializer, ShortlistCandidatesSerializer, ShortlistCandidatesSerializer,)
from accounts.serializers import UserViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from seeker.models import AppliedJobs
from seeker.serializers import AppliedJobsGetSerializer, ShortlistCandidatesGetSerializer
from django.utils import timezone






# Create your views here.




class CompanyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        id = request.query_params['id']

        try:
            profile = Company.objects.get(id=id)
            print('try workded')
            print(request.user.first_name)
            serializer = CompanyProfileSerializerGet(profile, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            print('data not found')
            return Response({'Message' : 'Data not found'}, status=status.HTTP_400_BAD_REQUEST)


class CompanyUpdateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def put(self, request:Response):
        id = request.query_params['id']

        profile = Company.objects.get(id=id)
        category = dict(request.data)['category'][0]
        category = CompanyCategory.objects.get(category_name=category)

        serializer = CompanyProfileSerializer(instance=profile, data=request.data)
        serializer2 = UserViewSerializer(instance=request.user, data=request.data)

        if serializer.is_valid() & serializer2.is_valid():
            serializer.save()
            serializer2.save()

            profile.category = category
            profile.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            print(serializer2.errors)
            return Response({'message': 'Profile updation failed'}, status=status.HTTP_400_BAD_REQUEST)




class UpdateView(APIView):
    
    def put(self, request:Response):
        id = request.query_params['id']

        profile = Account.objects.get(id=id)
        serializer = UserViewSerializer(instance=profile, data=request.data)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'done'})
        else:
            print(serializer.errors)
            return Response({'message': 'Not'})



class PostJobView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request:Response):
        print(request.data)

        serializer = PostJobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        id = request.query_params['id']
        print(request.data)

        try:
            company = Company.objects.get(id=id)
            jobs = Job.objects.filter(company_id = company)

            serializer = JobSerializerGet(jobs, many =True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except:
            print("not")
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SingleJobView(APIView):
    
    # permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        id = request.query_params['id']
        print(id)
        try:
            job = Job.objects.get(id=id)

            serializer = JobSerializerGet(job, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except:
            print("erroor")
            return Response(status=status.HTTP_400_BAD_REQUEST)


class JobUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request: Response):

        id = request.query_params['id']
        print(request.data)


        # try:
        job = Job.objects.get(id=id)
        print(job)
        serializer = PostJobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"message": "Job Updated successfully"}, status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            print('error')
            return Response(status=status.HTTP_400_BAD_REQUEST)


class JobDeleteView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        id = request.query_params['id']
        
        try:
            job = Job.objects.get(id=id)
            job.delete()

            return Response({"message": "Job deleted successfully"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"message": "Invalid id"}, status=status.HTTP_400_BAD_REQUEST)
        

class QualificationsView(APIView):
    
    def get(self, request:Response):
        qualifications = Qualification.objects.all()
        serializers = QualificationSerializer(qualifications, many=True)

        return Response(data=serializers.data, status=status.HTTP_200_OK)
    

class MembershipPurchaseView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request:Response):
        user_id = request.query_params['user_id']
        try:
            user = Company.objects.get(id=user_id)
            instance = MembershipPurchase.objects.filter(user=user, is_active=True)
            if instance:
                instance=MembershipPurchase.objects.get(user=user, is_active=True)            
                serializer = MembershipPurchaseSerializer(instance, many=False)
            else:
                return Response(data=None, status=status.HTTP_200_OK)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "No Data found"})


    def post(self, request:Response):
        data = request.data
        duration = data['duration']
        membership_id = UserMembership.objects.get(duration=duration).id
        data['membership'] = membership_id
        user_id = request.data['user']
        if MembershipPurchase.objects.filter(user=user_id).exists():
            obj = MembershipPurchase.objects.get(user=user_id)
            obj.membership = UserMembership.objects.get(id=membership_id)
            obj.save()
            serializer = SubsciptionPlanSerializer(data={'user':obj.id})
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Plan Updated successfully"}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response({"message": "subsciption failed"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = MembershipPurchaseSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                serializer = SubsciptionPlanSerializer(data={'user':user.id})
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
                    return Response({"message": "subsciption failed"}, status=status.HTTP_400_BAD_REQUEST)

                return Response({"message": "Plan subscribed successfully"}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response({"message": "subsciption failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class PlanDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
            user_id = request.query_params['user_id']
        # try:
            user = Company.objects.get(id=user_id)
            membership = MembershipPurchase.objects.get(user=user)

            instance = SubscriptionPlan.objects.filter(user=membership).order_by('-id')
            now = timezone.now().date()

            
            if now > instance[0].expiry_date and instance[0].is_active:
                obj = SubscriptionPlan.objects.get(id=instance[0].id)
                obj.is_active = False
                obj.save()
                print('done---------------------------------------------------------------------------------------')
            print(instance)

            serilaizer = SubsciptionPlanGetSerializer(instance, many=True)
            return Response(data=serilaizer.data, status=status.HTTP_200_OK)
        
        # except:
        #     return Response({"message", "Data not found"}, status=status.HTTP_400_BAD_REQUEST)

 
class ApplicationTrackingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        job_id = request.query_params['job_id']
        
        applied_jobs = AppliedJobs.objects.filter(job_id=job_id)
        if applied_jobs:
            serializer = AppliedJobsGetSerializer(applied_jobs, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=[], status=status.HTTP_200_OK)
        


class ApplicantShortlisiView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request:Response):

        applied_job = request.data['applied_job']
        if ShortlistedCandidates.objects.filter(applied_job=applied_job).exists():
            print('exists')
            return Response({"message": "Already shortlisted"})
        serializer = ShortlistCandidatesSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            instance = AppliedJobs.objects.get(id=applied_job)
            instance.is_shortlisted = True
            instance.save()
            return Response({"message": "Shortlisted Successfully"}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({"message": "Shorlisting Failed"}, status=status.HTTP_400_BAD_REQUEST)


class ShortlistedApplicantView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        recruiter = request.query_params['recruiter_id']
        try:
            recruiter = Company.objects.get(id=recruiter)
            shortlisted = ShortlistedCandidates.objects.filter(recruiter_id=recruiter)
            serialzer = ShortlistCandidatesGetSerializer(instance=shortlisted, many=True)
            return Response(data=serialzer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "data not found"}, status=status.HTTP_400_BAD_REQUEST)


class RemoveShortlistedCandidateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        id = request.query_params['applicant_id']
        instance = ShortlistedCandidates.objects.get(id=id)
        instance.delete()

        return Response({"message": "Applicant removed successfully"}, status=status.HTTP_200_OK)


        

    







    



