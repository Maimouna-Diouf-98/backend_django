from rest_framework import serializers
from .models import CustomDoctor,JourEtHeure

class DoctorSerializer(serializers.ModelSerializer):
    class Meta():
      model=CustomDoctor
      fields =('id','name',' proffession','adresse','experience','about',' jours_disponibles')
class CreateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDoctor
        fields = '__all__'
        extra_kwargs = {
            'jours_disponibles': {
                'required': True,
            },
            'name': {
                'required': True,
            },
        }

    def create(self, validated_data):
        name = validated_data.get('name')
        proffession = validated_data.get('proffession')
        adresse = validated_data.get('adresse')
        experience = validated_data.get('experience')
        about = validated_data.get('about')
        jours_disponibles = validated_data.get('jours_disponibles')
        doctor = CustomDoctor.objects.create_user(name=name, proffession=proffession, adresse=adresse, experience=experience, about=about, jours_disponibles=jours_disponibles)
        return doctor



class JourEtHeureSerialiser(serializers.ModelSerializer):
       doctor = CreateDoctorSerializer(many=True, read_only=True)
       model = JourEtHeure
       fields =('jours','heure','modele','id','doctor')
       def create(self, validated_data):
        jours = validated_data.get('jours')
        heure = validated_data.get('heure')
        modele = validated_data.get('modele')
        doctor = validated_data.get('doctor')
        jour = CustomDoctor.objects.create_user(jours=jours, heure=heure, modele=modele, 
          doctor=doctor)
        return doctor