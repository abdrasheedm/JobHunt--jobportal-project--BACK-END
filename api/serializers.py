from rest_framework import serializers
from .models import Me, You





# class YouViewSerialzer(serializers.ModelSerializer):
#     # me = MeViewSerializer()
#     class Meta:
#         model = You
#         fields = '__all__'

# class MeViewSerializer(serializers.ModelSerializer):
#     me__you = YouViewSerialzer()
#     class Meta:
#         model = Me
#         fields = ['id', 'name', 'me__you']