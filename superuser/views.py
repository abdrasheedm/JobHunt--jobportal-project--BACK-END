from django.shortcuts import render
from .serializers import CompanyCategorySerializer, CategoryDepartmentSerializer
from rest_framework.viewsets import ModelViewSet
from .models import CompanyCategory, CompanyDepartment
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView



# Create your views here.

class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer


class CompanyDepartmentView(APIView):
    

    def get(self, request:Response):

        id = request.query_params['id']
        print(request.data)

        try:
            category = CompanyCategory.objects.get(id = id)
            departments = CompanyDepartment.objects.filter(category=category)

            serializer = CategoryDepartmentSerializer(departments, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except:
            print("data not found")
            return Response(status=status.HTTP_400_BAD_REQUEST)
