from rest_framework import serializers
from .models import CustomRendezVous,Carte

#  serialiser carte
class CarteSerializer(serializers.ModelSerializer):
  class Meta():
        model = Carte
        fields = '__all__'
class RendezVousSerializer(serializers.ModelSerializer):
    carte =serializers.PrimaryKeyRelatedField(many=True, queryset=Carte.objects.all())
    class Meta():
        model = CustomRendezVous
        fields = '__all__'

class RendezVousDetailSerializer(serializers.ModelSerializer):
    carte =CarteSerializer(many=True)
    class Meta():
        model = CustomRendezVous
        fields = '__all__'
