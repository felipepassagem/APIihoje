from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()  # Use 'email' instead of 'username'
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    token = serializers.CharField(read_only=True)
