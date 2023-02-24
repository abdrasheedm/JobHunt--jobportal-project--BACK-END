from rest_framework import serializers
from .models import Notifications


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notifications
        fields = '__all__' 


# class NotificationUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Notifications
#         fields = ['is_seen']

#     def update(self, instances):
#         for instance in instances:
#             instance.is_seen =True
#             instance.save()

#             return instance