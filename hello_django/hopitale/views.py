from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import HopitalSerializer,JourSerializer,SpecialistSerializer
from .models import CustomHopitale,Jour_hopitale,Specialist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class HopitalAPI(APIView):
     def post(self, request, format=None):
        serializer = HopitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#get all hopital 
@api_view(['GET'])
def hopital_list(request):
    if request.method == 'GET':
        hopital = CustomHopitale.objects.all()
        serializer = HopitalSerializer(hopital, many=True)
        return Response(serializer.data)

#  get one Hopital
@api_view(['GET'])
def list_id_hopital(request, pk):
    try:
        hopital = CustomHopitale.objects.get(pk=pk)
    except hopital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HopitalSerializer(hopital)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
#  update HOPITal
# update
@api_view(['PUT'])
def update_hopital(request, pk):
    try:
        hopital = CustomHopitale.objects.get(pk=pk)
    except CustomHopitale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = HopitalSerializer(hopital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# delete hopital
@api_view(['DELETE'])
def delete_hopital(request, pk):
    try:
       hopital  = CustomHopitale.objects.get(pk=pk)
    except CustomHopitale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        hopital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# Create jour

class JourAPI(APIView):
  def post(self, request, format=None):
        serializer = JourSerializer(data=request.data)
        if serializer.is_valid():
            jour = serializer.validated_data.get('jour') 
            jour_exist=Jour_hopitale.objects.filter(jour=jour).exists()
            if jour_exist :
              return Response({'erreur': 'Le jour existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def jour_list(request):
    if request.method == 'GET':
        jour= Jour_hopitale.objects.all()
        serializer = JourSerializer(jour, many=True)
        return Response(serializer.data)

#  get one day
@api_view(['GET'])
def list_id_jour(request, pk):
    try:
        jour = Jour_hopitale.objects.get(pk=pk)
    except Jour_hopitale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JourSerializer(jour)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
       
# update
@api_view(['PUT'])
def update_jour(request, pk):
    try:
        jour = Jour_hopitale.objects.get(pk=pk)
    except Jour_hopitale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = JourSerializer(jour, data=request.data)
        if serializer.is_valid():
            jour = serializer.validated_data.get('jour') 
            jour_exist=Jour_hopitale.objects.filter(jour=jour).exists()
            if jour_exist :
              return Response({'erreur': 'Le jour existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update day
# Create your Specialisation.
class SpecialistAPI(APIView):
     def post(self, request, format=None):
        serializer = SpecialistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get specialist
@api_view(['GET'])
def special_list(request):
    if request.method == 'GET':
        specialist = Specialist.objects.all()
        serializer = SpecialistSerializer(specialist, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def list_id_special(request, pk):
    try:
        specialist = Specialist.objects.get(pk=pk)
    except Specialist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpecialistSerializer(specialist)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
      