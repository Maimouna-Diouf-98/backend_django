from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomRendezVous,Carte
from .serializers import RendezVousSerializer,CarteSerializer,RendezVousDetailSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
# create render_vous
class RendezVousAPI(generics.CreateAPIView):
    queryset = CustomRendezVous.objects.all()
    serializer_class = RendezVousSerializer 
    def post(self, request, format=None):
     data = request.data
     carte_id = data.get('carte', []) 
     serializer = self.get_serializer(data=data)
     if serializer.is_valid():
        self.perform_create(serializer)
        rendez_vous = CustomRendezVous.objects.get(id=serializer.data['id'])
        carte = Carte.objects.filter(id__in=carte_id)
        rendez_vous.carte.set(carte)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get all rendervous
class ListRendezVousAPI(generics.ListAPIView):
     queryset = CustomRendezVous.objects.all()
     serializer_class = RendezVousDetailSerializer
     def get(self, request, format=None):
        rendez_vous = CustomRendezVous.objects.all()
        serializer = RendezVousDetailSerializer(rendez_vous, many=True)
        return Response(serializer.data)
#  get one rendez vous
@api_view(['GET'])
def list_id_rendez_vous(request, pk):
    try:
        rendez_vous = CustomRendezVous.objects.get(pk=pk)
    except CustomRendezVous.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RendezVousDetailSerializer(rendez_vous)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
# update rendez vous
class RendezVousUpdate(generics.UpdateAPIView):
    queryset = CustomRendezVous.objects.all()
    serializer_class = RendezVousSerializer
# delete rendez vous                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
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
class CarteAPI(generics.CreateAPIView):
     queryset = Carte.objects.all()
     serializer_class = CarteSerializer 
     def post(self, request, format=None):
        serializer = CarteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get all carte
class ListCarteAPI(generics.ListAPIView):
     queryset = Carte.objects.all()
     serializer_class = CarteSerializer
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
class CarteUpdate(generics.UpdateAPIView):
    queryset = Carte.objects.all()
    serializer_class = CarteSerializer 
