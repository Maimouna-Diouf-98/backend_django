from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomRendezVous
from .serializers import RendezVousSerializer
from rest_framework.decorators import api_view

class RendezVousAPI(APIView):
    def post(self, request, format=None):
        serializer = RendezVousSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListRendezVousAPI(APIView):
     def get(self, request, format=None):
        rendez_vous = CustomRendezVous.objects.all()
        serializer = RendezVousSerializer(rendez_vous, many=True)
        return Response(serializer.data)

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
