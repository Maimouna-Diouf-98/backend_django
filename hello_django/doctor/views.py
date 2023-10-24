from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import DoctorSerializer,JourSerializer
from .models import CustomDoctor,Jour_Doctor
from rest_framework import status


# # Create your views here.
#  create doctor
class CreateDoctorAPI(APIView):
     def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
# update
@api_view(['PUT'])
def update_doctor(request, pk):
    try:
        doctor = CustomDoctor.objects.get(pk=pk)
    except CustomDoctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#  delete a doctor
@api_view(['DELETE'])
def delete_doctor(request, pk):
    try:
        doctor = CustomDoctor.objects.get(pk=pk)
    except doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
# # Create jour
class JourAPI(APIView):
  def post(self, request, format=None):
        serializer = JourSerializer(data=request.data)
        if serializer.is_valid():
            jour = serializer.validated_data.get('jour') 
            jour_exist=Jour_Doctor.objects.filter(jour=jour).exists()
            if jour_exist :
              return Response({'erreur': 'Le jour existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
# update
@api_view(['PUT'])
def update_jour(request, pk):
    try:
        jour = Jour_Doctor.objects.get(pk=pk)
    except Jour_Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = JourSerializer(jour, data=request.data)
        if serializer.is_valid():
            jour = serializer.validated_data.get('jour') 
            jour_exist=Jour_Doctor.objects.filter(jour=jour).exists()
            if jour_exist :
              return Response({'erreur': 'Le jour existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
