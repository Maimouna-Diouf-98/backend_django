from rest_framework import serializers
from .models import CustomHopitale,Jour_hopitale

class JourHopitalSerializer(serializers.ModelSerializer):
    class Meta():
        model = Jour_hopitale
        fields = '__all__'
class JourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jour_hopitale
        fields = '__all__'
    def create(self, validated_data):
        jour = validated_data.get('jour')
        heure_debut = validated_data.get('heure_debut')
        heure_fin = validated_data.get('heure_fin')
        jour= Jour_hopitale.objects.create_user(jour=jour,  heure_fin= heure_fin,heure_debut=heure_debut)
        return jour
# create hopital 
class HopitalSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomHopitale
        fields = '__all__'

class CreateHopitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomHopitale
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': True,
            },
        }
    def create(self, validated_data):
        name = validated_data.get('name')
        specialist = validated_data.get('specialist')
        adresse = validated_data.get('adresse')
        jours = validated_data.get('jours',[])
        about = validated_data.get('about')
        heure  = validated_data.get('heure')
        date  = validated_data.get('date')
        image = validated_data.get('image')
      
        hopital = CustomHopitale.objects.create_user(name=name, adresse=adresse,
           date=date, heure=heure , about=about, specialist=specialist, image=image)
        if hopital :
            hopital.jours.set(jours)   
        return hopital



