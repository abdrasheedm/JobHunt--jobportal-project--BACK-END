from django.shortcuts import render
from rest_framework import status
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import Account
from .models import Notifications



# Create your views here.


class NotificatinView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request:Response):
        user_id = request.query_params['user_id']
        user = Account.objects.get(id=user_id)
        notifications = Notifications.objects.filter(user=user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
 