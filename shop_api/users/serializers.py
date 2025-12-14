from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmCode


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise ValidationError("User already exists! ")
        except User.DoesNotExist:
            return username

    

class ConfirmCodeSerializer(serializers.Serializer):
    confirm_code = serializers.CharField(max_length=6)

    def validate_code(self,confirm_code):
        try:
              ConfirmCode.objects.get(confirm_code=confirm_code)
              return confirm_code
        except ConfirmCode.DoesNotExist:
            raise ValidationError('This code does not exist')

