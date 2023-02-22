from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import Account
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import SeekerProfile, Education, Experience, SeekerSkillSet, Projects, FavouriteJob, AppliedJobs
from .serializers import (SeekerProfileSerializer, SeekerProfileUpdateSerializer, EducationSerilizer, ExperienceSerializer, ProjectSerializer, ApplyJobSerializer,
                          FavouriteJobSerializer, FavouriteJobGetSerializer, AppliedJobsGetSerializer)
from recruiter.models import Job
from recruiter.serilaizers import JobSerializerGet




# Create your views here.

class SeekerProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


    def get(self, request:Response):
        id = request.query_params['id']

        try:
            profile = SeekerProfile.objects.get(id=id)
            print('try worked')
            serializer = SeekerProfileSerializer(profile, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except:
            print('data not found')
            return Response({'message': 'Data not found'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request:Response):
        id = request.query_params['id']
        profile = SeekerProfile.objects.get(id = id)
        serializer = SeekerProfileSerializer(instance=profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': "updaded successfully"})
        else:
            print("else worked")
            return Response({'message':'Failed'})
        


class SeekerProfileUpdateView(APIView):
    
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


    def put(self, request:Response):
        id = request.query_params['id']
        print(request.data)
        profile = SeekerProfile.objects.get(id = id)
        serializer = SeekerProfileUpdateSerializer(instance=profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': "updaded successfully"})
        else:
            print(serializer.errors)
            return Response({'message':'Failed'})
        


class AllSeekersGetView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        seekers = SeekerProfile.objects.all()
        serializers = SeekerProfileSerializer(instance=seekers, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
        

class PostEducationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request:Response):
        print(request.data)

        serializer = EducationSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"message": "Posted successfully"}, status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            return Response({"message": "Updation Failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class SeekerEducationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        id = request.query_params['id']
        try:
            instance = Education.objects.get(id=id)
            serializer = EducationSerilizer(instance=instance, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
           
        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)



class UpdateEducationView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request:Response):

        id = request.query_params['id']
        try:
            instance = Education.objects.get(id=id)

            serializer = EducationSerilizer(instance=instance, data=request.data, partial = True)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Education updated succesfully"}, status=status.HTTP_200_OK)

            else:
                print(serializer.data)
                return Response({"message": "Education updation failed"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)




class PostExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request:Response):
        print(request.data)

        serializer = ExperienceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"message": "Posted successfully"}, status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            return Response({"message": "Adding failed Failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class SeekerExperienceSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        id = request.query_params['id']
        try:
            instance = Experience.objects.get(id=id)
            serializer = ExperienceSerializer(instance=instance, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
           
        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        


class SeekerExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        id = request.query_params['id']
        try:
            instance = Experience.objects.filter(user_id=id)
            serializer = ExperienceSerializer(instance=instance, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
           
        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        





class UpdateExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request:Response):

        id = request.query_params['id']
        try:
            instance = Experience.objects.get(id=id)
            serializer = ExperienceSerializer(instance=instance, data=request.data, partial = True)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Experience updated succesfully"}, status=status.HTTP_200_OK)

            else:
                print(serializer.data)
                return Response({"message": "Education updation failed"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        

class DeleteExperienceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        id = request.query_params['exp_id']
        
        try:
            instance = Experience.objects.get(id=id)
            instance.delete()

            return Response({"message": "Experience deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Invalid experience data"}, status=status.HTTP_400_BAD_REQUEST)




class PostProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request:Response):
        print(request.data)

        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"message": "Posted successfully"}, status=status.HTTP_200_OK)

        else:
            print(serializer.errors)
            return Response({"message": "Adding Project Failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class SeekerProjectSingleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        id = request.query_params['id']
        try:
            instance = Projects.objects.get(id=id)
            serializer = ProjectSerializer(instance=instance, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
           
        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        


class SeekerProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        id = request.query_params['id']
        try:
            instance = Projects.objects.filter(user_id=id)
            serializer = ProjectSerializer(instance=instance, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
           
        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        





class UpdateProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request:Response):

        id = request.query_params['id']
        try:
            instance = Projects.objects.get(id=id)
            serializer = ProjectSerializer(instance=instance, data=request.data, partial = True)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Project updated succesfully"}, status=status.HTTP_200_OK)

            else:
                print(serializer.data)
                return Response({"message": "Project updation failed"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"message": "Id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        


class DeleteProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        id = request.query_params['proj_id']
        
        try:
            instance = Projects.objects.get(id=id)
            instance.delete()

            return Response({"message": "Project deleted Successfully"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Invalid experience data"}, status=status.HTTP_400_BAD_REQUEST)
        
        


class BrowseJobsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        jobs = Job.objects.filter(is_active=True)
        serializer = JobSerializerGet(jobs, many=True)

     
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        




class ApplyJobView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


    def post(self, request:Response):

        serializer = ApplyJobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Applied Successfully"}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class AppliedJobsView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        print(request.query_params)

        if 'seeker_id' in dict(request.query_params):
            seeker_id = request.query_params['seeker_id']
            jobs = AppliedJobs.objects.filter(seeker_id=seeker_id)
        else:
            recruiter_id = request.query_params['recruiter_id']
            jobs = AppliedJobs.objects.filter(recruiter_id=recruiter_id)


        serializers = AppliedJobsGetSerializer(instance=jobs, many=True)

        return Response(data=serializers.data, status=status.HTTP_200_OK)
    


class AppliedJobRemoveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        job_id = request.query_params['job_id']
        seeker_id = request.query_params['user_id']
        print(job_id)

        try:
            job = AppliedJobs.objects.get(job_id=job_id, seeker_id=seeker_id)
            job.delete()
            return Response({"message": "Remoed From Applied Jobs"}, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



        


class FavouriteJobView(APIView):
    permission_classes = [IsAuthenticated]    

    def post(self, request:Response):

        try:
            job_id = request.query_params['job_id']
            seeker_id = request.query_params['seeker_id']

            to_remove = FavouriteJob.objects.get(job_id=job_id, seeker_id=seeker_id)
            to_remove.delete()

            return Response({"message": "Removed From Favourites"})
        
        except:
            serializer = FavouriteJobSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Added to Favourite Jobs"}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        

class FavouriteJobGetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        
        id = request.query_params['id']
        print(id)

        try:
            favourites = FavouriteJob.objects.filter(seeker_id=id)
            serializers = FavouriteJobSerializer(instance=favourites, many=True)

            return Response(data=serializers.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "Invalid Id"})


class RemoveFavouritedJobView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        job_id = request.query_params['job_id']
        seeker_id = request.query_params['seeker_id']

        to_remove = FavouriteJob.objects.get(job_id=job_id, seeker_id=seeker_id)
        to_remove.delete()

        return Response({"message": "Removed Successfully"})
    

class FavouriteJobListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Response):

        seeker_id = request.query_params['seeker_id']
        try:
            favourites = FavouriteJob.objects.filter(seeker_id=seeker_id)

            print(seeker_id, favourites)

            serializers = FavouriteJobGetSerializer(instance=favourites, many=True)

            return Response(data=serializers.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "No jobs found"})
        


