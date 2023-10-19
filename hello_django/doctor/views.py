from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView
from django.views.generic.list import ListView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import  CreateDoctorSerializer,UpdateDoctorSerializer,DoctorSerializer,JourSerializer,UpdateJourSerializer
from .models import CustomDoctor,Jour_Doctor
from rest_framework import status


# # Create your views here.
#  create doctor
class CreateDoctorAPI(CreateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = CreateDoctorSerializer
    premission_classes = (AllowAny,)

#  get all doctors
@api_view(['GET'])
def doctors_list(request):
    if request.method == 'GET':
        doctor = CustomDoctor.objects.all()
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

#  get one doctor
@api_view(['GET'])
def list_id_doctor(request, pk):
    try:
        doctor = CustomDoctor.objects.get(pk=pk)
    except doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)

#  update doctor
class UpdateDoctorAPI(UpdateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = UpdateDoctorSerializer
    
#  delete a doctor
@api_view(['DELETE'])
def delete_doctor(request, pk):
    try:
        doctor = CustomDoctor.objects.get(pk=pk)
    except doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        doctor.delete()
       
# Create jour
class JourAPI(CreateAPIView):
    queryset = Jour_Doctor.objects.all()
    serializer_class = JourSerializer
    premission_classes = (AllowAny,)

@api_view(['GET'])
def jour_list(request):
    if request.method == 'GET':
        jour= Jour_Doctor.objects.all()
        serializer = JourSerializer(jour, many=True)
        return Response(serializer.data)

#  get one day
@api_view(['GET'])
def list_id_jour(request, pk):
    try:
        jour = Jour_Doctor.objects.get(pk=pk)
    except Jour_Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JourSerializer(jour)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
# update day
class UpdateJourAPI(UpdateAPIView):
    queryset = Jour_Doctor.objects.all()
    serializer_class = UpdateJourSerializer
    