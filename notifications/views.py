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

    def get(self, request:Response):
        user_id = request.query_params['user_id']
        user = Account.objects.get(id=user_id)
        notifications = Notifications.objects.filter(user=user).order_by('-id')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class UnreadNotificationCountView(APIView):

    def get(self, request:Response):
        user_id = request.query_params['user_id']
        count = Notifications.objects.filter(user=user_id, is_seen = False).count()
        print(count)
        return Response(data={'count':count}, status=status.HTTP_200_OK)
    

class UpdateNotificationView(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request:Response):

        user_id = request.query_params['user_id']
        instances = Notifications.objects.filter(user=user_id, is_seen = False)
        if instances:
            for instance in instances:
                instance.is_seen = True
                instance.save()

        return Response({"messgae": "updated unread messages"}, status=status.HTTP_200_OK)

    

 