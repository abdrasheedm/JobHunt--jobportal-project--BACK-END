from rest_framework import serializers
from .models import CompanyCategory



class CompanyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCategory
        fields = ['category_name']