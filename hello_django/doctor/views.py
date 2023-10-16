from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import  CreateDoctorSerializer,JourEtHeureSerialiser
from .models import CustomDoctor, JourEtHeure
from rest_framework import status

# Create your views here.
class CreateDoctorAPI(CreateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = CreateDoctorSerializer
    premission_classes = (AllowAny,)
    
class JourEtHeure(CreateAPIView):
    queryset = JourEtHeure.objects.all()
    serializer_class = JourEtHeureSerialiser
    premission_classes = (AllowAny,)