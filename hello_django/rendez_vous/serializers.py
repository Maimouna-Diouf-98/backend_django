from rest_framework import serializers
from .models import CustomRendezVous,Carte

#  serialiser carte
class CarteSerializer(serializers.ModelSerializer):
  class Meta():
        model = Carte
        fields = '__all__'
class RendezVousSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomRendezVous
        fields = '__all__'
