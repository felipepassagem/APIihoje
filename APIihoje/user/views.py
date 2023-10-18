from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomUser
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import AuthTokenSerializer



class CustomUserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     print("ASDASDASDASDASDASDASDASDASDASDASDASDASDclear")
    #     token, created = Token.objects.get_or_create(user=user)

  # Importe o seu serializer personalizado

class EmailLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)  # Use seu serializer personalizado
        if serializer.is_valid():
            user_email = serializer.validated_data['email']
            user = CustomUser.objects.get(email=user_email)
            # user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

