from rest_framework import serializers
from .models import Account, UserType
from rest_framework.validators import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
User = get_user_model()


# class UserTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserType
#         fields = '__all__'



class SignUpSerializer(serializers.ModelSerializer):
 
    # user_type = UserTypeSerializer

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')

    def validate(self, attrs):
        #email validation
        is_email_exist = Account.objects.filter(email = attrs['email']).exists()

        if is_email_exist:
            return ValidationError('This email is already taken')
        return super().validate(attrs)

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError as e:
            print("email not valid, details:", e)
            raise serializers.ValidationError("This is not a valid email, try again !")
        else:
            print("good email")
        
        return value

    def create(self, validated_data):
        # hashing password
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user



class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'



class UserViewSerializer(serializers.ModelSerializer):
    # user_type = UserTypeSerializer()
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email']




