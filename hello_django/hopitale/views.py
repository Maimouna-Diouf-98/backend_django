from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import HopitalSerializer,JourSerializer,SpecialistSerializer,ListHopitalSerializer
from .models import CustomHopitale,Jour_hopitale,Specialist
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


# Create your views here.
# create hopital 
class HopitalAPI(generics.CreateAPIView):
    queryset = CustomHopitale.objects.all()
    serializer_class = HopitalSerializer 
    def post(self, request, format=None):
     data = request.data
     jours_id = data.get('jours', [])
     specialist_id = data.get('specialist', [])
     serializer = self.get_serializer(data=data)
     if serializer.is_valid():
        self.perform_create(serializer)
        hopital = CustomHopitale.objects.get(id=serializer.data['id'])
        jours = Jour_hopitale.objects.filter(id__in=jours_id)
        specialist = Specialist.objects.filter(id__in=specialist_id)
        hopital.jours.set(jours)
        hopital.specialist.set(specialist)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
#get all hopital 
class HopitalListView(generics.ListAPIView):
    queryset = CustomHopitale.objects.all()
    serializer_class =  ListHopitalSerializer
#  get one Hopital
@api_view(['GET'])
def list_id_hopital(request, pk):
    try:
        hopital = CustomHopitale.objects.get(pk=pk)
    except hopital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListHopitalSerializer(hopital)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
#  update HOPITal
class HopitalUpdate(generics.UpdateAPIView):
    queryset = CustomHopitale.objects.all()
    serializer_class = HopitalSerializer 
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
        

# # Create jour
class JourAPI(generics.CreateAPIView):
  queryset = Jour_hopitale.objects.all()
  serializer_class = JourSerializer 
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
# get all day
class JourListView(generics.ListAPIView):
    queryset = Jour_hopitale.objects.all()
    serializer_class =  JourSerializer
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
       
# update day
class JourUpdate(generics.UpdateAPIView):
    queryset = Jour_hopitale.objects.all()
    serializer_class = JourSerializer 
# Create your Specialisation.
class SpecialistAPI(generics.CreateAPIView):
     queryset = Specialist.objects.all()
     serializer_class = SpecialistSerializer 
     def post(self, request, format=None):
        serializer = SpecialistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get all specialist
class SpecialListView(generics.ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class =  SpecialistSerializer
# get one special
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
            
# update specialist
class SpecialUpdate(generics.UpdateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer 
