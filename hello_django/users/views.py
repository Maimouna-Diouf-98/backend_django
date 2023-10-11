from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import  CreateUserSerializer,UpdateUserSerializer,LoginSerializer
from .models import CustomUser
from knox import views as knox_views
from django.contrib.auth import login ,logout
from knox.views import LogoutView
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from knox.models import AuthToken

# Create your views here.
class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    premission_classes = (AllowAny,)


class UpdateUserAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer

class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response.data,status = status.HTTP_200_OK)

class LogoutAPI(APIView):
     authentication_classes = (TokenAuthentication,)
     def post(self, request):
        logout(request) 
        return Response({'message': "Déconnexion réussie"}, status=status.HTTP_200_OK)
     
    