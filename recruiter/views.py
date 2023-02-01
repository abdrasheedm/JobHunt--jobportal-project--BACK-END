from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Company, Job
from superuser.models import CompanyCategory, CompanyDepartment
from superuser.serializers import CompanyCategorySerializer
from accounts.models import Account
from .serilaizers import CompanyProfileSerializerGet, CompanyProfileSerializer, PostJobSerializer,  JobSerializerGet
from accounts.serializers import UserViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics





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
        print(request.data)

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
    
    permission_classes = [IsAuthenticated]

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



    



