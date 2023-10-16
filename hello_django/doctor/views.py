from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import  CreateDoctorSerializer, DoctorSerializer
from .models import CustomDoctor
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def DoctorList(request):
    doctors = CustomDoctor.objects.all()
    serializer = DoctorSerializer(doctors, many=False)

@api_view(['POST'])
def CreateDoctor(request):
    serializer = CreateDoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

