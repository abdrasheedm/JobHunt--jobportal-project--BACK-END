from django.shortcuts import render
from .serializers import CompanyCategorySerializer, CategoryDepartmentSerializer, AlluserViewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import CompanyCategory, CompanyDepartment
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from accounts.models import Account
# from rest_framework.generics import ListAPIView



# Create your views here.

class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyDepartmentView(APIView):
    

    def get(self, request:Response):

        try:
            id = request.query_params['id']
            print(request.data)
            category = CompanyCategory.objects.get(id = id)
            departments = CompanyDepartment.objects.filter(category=category)

            serializer = CategoryDepartmentSerializer(departments, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except:
            departments = CompanyDepartment.objects.all()
            serializer = CategoryDepartmentSerializer(departments, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)



class AllUserGet(ModelViewSet):
    permission_classes = [IsAdminUser]
    
    queryset = Account.objects.all()
    serializer_class = AlluserViewSerializer

