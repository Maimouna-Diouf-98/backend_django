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
    def validate(self,  attrs):
        jour = attrs.get('jour')
        if  Jour_hopitale.objects.filter(jour=jour).exists():
            raise serializers.ValidationError('jour exist.')
    def create(self, validated_data):
        jour = validated_data.get('jour')
        heure_debut = validated_data.get('heure_debut')
        heure_fin = validated_data.get('heure_fin')
        jours= Jour_hopitale.objects.create_user(jour=jour,  heure_fin= heure_fin,heure_debut=heure_debut)
        return jours

class UpdateJourSerializer(serializers.ModelSerializer):
     class Meta():
        model = Jour_hopitale
        fields ='__all__'
     def update(self,instance,validated_data):
       instance.heure_debut= validated_data.get('heure_debut', instance.heure_debut)
       instance.heure_fin = validated_data.get('heure_fin', instance.heure_fin)
       instance.save()
       return instance
     
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
            "password": {
                 'required':False,  
              }
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
        note = validated_data.get('note')
      
        hopital = CustomHopitale.objects.create_user(name=name, adresse=adresse,
           date=date, heure=heure , about=about, specialist=specialist, image=image, note=note)
        if hopital :
            hopital.jours.set(jours)   
        return hopital


class UpdateHopitalSerializer(serializers.ModelSerializer):
     class Meta():
        model = CustomHopitale
        fields ='__all__'
     def update(self,instance,validated_data):
       instance.name = validated_data.get('name', instance.name)
       instance.specialist = validated_data.get('specialist', instance.specialist)
       instance.adresse = validated_data.get('adresse', instance.adresse)
       instance.about= validated_data.get('about', instance.about)
       instance.heure= validated_data.get('heure', instance.heure)
       instance.date= validated_data.get('date', instance.date)
       instance.note= validated_data.get('note', instance.note)
       instance.image= validated_data.get('image', instance.image)
       jours_ids = self.validated_data.get('jours', [])
       instance.jours.set(jours_ids)
       instance.save()
       return instance

