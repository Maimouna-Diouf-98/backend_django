from rest_framework import serializers
from .models import CustomDoctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta():
      model=CustomDoctor
      fields ='__all__'
class CreateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDoctor
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'required': True,
            },
        }
    def create(self, validated_data):
        name = validated_data.get('name')
        heure = validated_data.get('heure')
        jours = validated_data.get('jours')
        proffession = validated_data.get('proffession')
        adresse = validated_data.get('adresse')
        experience = validated_data.get('experience')
        about = validated_data.get('about')
        jours_disponibles = validated_data.get('jours_disponibles')
        doctor = CustomDoctor.objects.create_user(name=name, proffession=proffession, adresse=adresse,
          experience=experience, about=about, jours=jours,heure=heure)
        return doctor

class UpdateDoctorSerializer(serializers.ModelSerializer):
     class Meta():
        model = CustomDoctor
        fields ='__all__'
     def update(self,instance,validated_data):
       instance.name = validated_data.get('name', instance.name)
       instance.proffession = validated_data.get('proffession', instance.proffession)
       instance.adresse = validated_data.get('adresse', instance.adresse)
       instance.experience= validated_data.get('experience', instance.experience)
       instance.about= validated_data.get('about', instance.about)
       instance.jours= validated_data.get('jours', instance.jours)
       instance.heure= validated_data.get('heure', instance.heure)
       instance.save()
       return instance
