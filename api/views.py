# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Me, You
# from .serializers import MeViewSerializer, YouViewSerialzer


# # Create your views here.

# class MeView(APIView):
#     def get(self, request:Response):
#         query_set = Me.objects.all()
#         serializer = MeViewSerializer(query_set, many=True)

#         return Response(data=serializer.data)