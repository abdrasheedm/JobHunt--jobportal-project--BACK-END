from django.shortcuts import render
from .serializers import CompanyCategorySerializer
from rest_framework.viewsets import ModelViewSet
from .models import CompanyCategory
# Create your views here.

class CompanyCategoryView(ModelViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer
