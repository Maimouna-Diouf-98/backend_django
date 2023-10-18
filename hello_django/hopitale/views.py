from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .serializers import HopitalSerializer,CreateHopitalSerializer,JourSerializer
from .models import CustomHopitale,Jour_hopitale
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins

# Create your views here.
class HopitalAPI(CreateAPIView):
    queryset = CustomHopitale.objects.all()
    serializer_class = CreateHopitalSerializer
    premission_classes = (AllowAny,)
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
# update hopital
# class update_hopital():


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
class JourAPI(CreateAPIView):
    queryset = Jour_hopitale.objects.all()
    serializer_class = JourSerializer
    premission_classes = (AllowAny,)

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
    except hopital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JourSerializer(jour)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
