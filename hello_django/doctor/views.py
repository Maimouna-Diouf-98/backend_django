from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView
from django.views.generic.list import ListView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import  CreateDoctorSerializer,UpdateDoctorSerializer,DoctorSerializer
from .models import CustomDoctor
from rest_framework import status


# # Create your views here.

@api_view(['GET', 'POST'])
def doctors_list(request):
    if request.method == 'GET':
        doctor = CustomDoctor.objects.all()
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)
class CreateDoctorAPI(CreateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = CreateDoctorSerializer
    premission_classes = (AllowAny,)
class UpdateDoctorAPI(UpdateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = UpdateDoctorSerializer
