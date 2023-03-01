from django.shortcuts import render
from recruiter.models import Job
from rest_framework.views import APIView
from rest_framework.response import Response
from recruiter.serilaizers import JobSerializerGet
from rest_framework import status



# Create your views here.


class TopJobsView(APIView):

    def get(self, request:Response):
        top_jobs = Job.objects.all().order_by('-id')[:6]
        seriaizer = JobSerializerGet(top_jobs, many=True)
        return Response(data=seriaizer.data, status=status.HTTP_200_OK)

