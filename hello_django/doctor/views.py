from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import DoctorSerializer,JourSerializer,DoctorListSerializer
from .models import CustomDoctor,Jour_Doctor
from rest_framework import status

# # Create your views here.

#  create doctor
class CreateDoctorAPI(generics.CreateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = DoctorSerializer 
    def post(self, request, format=None):
     data = request.data
     jours_id = data.get('jours', []) 
     serializer = self.get_serializer(data=data)
     if serializer.is_valid():
        self.perform_create(serializer)
        doctor = CustomDoctor.objects.get(id=serializer.data['id'])
        jours = Jour_Doctor.objects.filter(id__in=jours_id)
        doctor.jours.set(jours)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#  get all doctors
class DoctorListView(generics.ListAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class =  DoctorListSerializer
#  get one doctor
@api_view(['GET'])
def list_id_doctor(request, pk):
    try:
        doctor = CustomDoctor.objects.get(pk=pk)
    except doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorListSerializer(doctor)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
# update doctor
class DoctorDetail(generics.UpdateAPIView):
    queryset = CustomDoctor.objects.all()
    serializer_class = DoctorSerializer 
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
class JourAPI(generics.CreateAPIView):
  queryset = Jour_Doctor.objects.all()
  serializer_class = JourSerializer 
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
# get all day 
class JourListView(generics.ListAPIView):
    queryset = Jour_Doctor.objects.all()
    serializer_class = JourSerializer
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
class JourUpdateView(generics.UpdateAPIView):
    queryset = Jour_Doctor.objects.all()
    serializer_class = JourSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            jour = serializer.validated_data.get('jour') 
            jour_exist = Jour_Doctor.objects.exclude(pk=instance.pk).filter(jour=jour).exists()
            if jour_exist:
                return Response({'erreur': 'Le jour existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




