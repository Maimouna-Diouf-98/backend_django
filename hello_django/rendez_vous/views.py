from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomRendezVous,Carte
from .serializers import RendezVousSerializer,CarteSerializer
from rest_framework.decorators import api_view
# create render_vous
class RendezVousAPI(APIView):
    def post(self, request, format=None):
        serializer = RendezVousSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get all rendervous
class ListRendezVousAPI(APIView):
     def get(self, request, format=None):
        rendez_vous = CustomRendezVous.objects.all()
        serializer = RendezVousSerializer(rendez_vous, many=True)
        return Response(serializer.data)
#  get one rendez vous
@api_view(['GET'])
def list_id_rendez_vous(request, pk):
    try:
        rendez_vous = CustomRendezVous.objects.get(pk=pk)
    except CustomRendezVous.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RendezVousSerializer(rendez_vous)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
# update rendez vous
@api_view(['PUT'])
def list_update(request, pk):
    try:
        rendez_vous = CustomRendezVous.objects.get(pk=pk)
    except CustomRendezVous.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RendezVousSerializer(rendez_vous, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete_rendez_vous(request, pk):
    try:
        rendez_vous = CustomRendezVous.objects.get(pk=pk)
    except CustomRendezVous.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        rendez_vous.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# create  carte 
class CarteAPI(APIView):
    def post(self, request, format=None):
        serializer = CarteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get all carte
class ListCarteAPI(APIView):
     def get(self, request, format=None):
        carte = Carte.objects.all()
        serializer = CarteSerializer(carte, many=True)
        return Response(serializer.data)
# get one carte
@api_view(['GET'])
def list_id_carte(request, pk):
    try:
        carte = Carte.objects.get(pk=pk)
    except Carte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarteSerializer(carte)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
# update carte
@api_view(['PUT'])
def carte_update(request, pk):
    try:
        carte = Carte.objects.get(pk=pk)
    except Carte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CarteSerializer(carte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        