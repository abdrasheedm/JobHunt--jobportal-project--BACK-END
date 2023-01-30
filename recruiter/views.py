from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Company
from superuser.models import CompanyCategory
from superuser.serializers import CompanyCategorySerializer
from accounts.models import Account
from .serilaizers import CompanyProfileSerializerGet, CompanyProfileSerializer
from accounts.serializers import UserViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser



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
        # recruiter = request.data.pop['recruiter']
        # print(dict1['recruiter'])
        category = dict(request.data)['category'][0]
        category = CompanyCategory.objects.get(category_name=category)

        serializer = CompanyProfileSerializer(instance=profile, data=request.data)
        serializer2 = UserViewSerializer(instance=request.user, data=request.data)

        if serializer.is_valid() & serializer2.is_valid():
            serializer.save()
            serializer2.save()

            print(serializer.data)
            print(serializer2.data)
            # category = CompanyCategory.objects.get(category_name = category['category_name'])
            # print(category)
            # user = request.user
            # user.first_name = recruiter['first_name']
            # user.last_name = recruiter['last_name']
            # user.email = recruiter['email']
            # user.phone_number = recruiter['phone_number']
            # user.save()
            profile.category = category
            profile.save()
            return Response({'message': 'done'})
        else:
            print(serializer.errors)
            return Response({'message': 'Not'})




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



    



