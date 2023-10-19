from rest_framework import serializers
from .models import CustomDoctor,Jour_Doctor
# doctor
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
        jours = validated_data.get('jours',[])
        proffession = validated_data.get('proffession')
        adresse = validated_data.get('adresse')
        experience = validated_data.get('experience')
        about = validated_data.get('about')
        image = validated_data.get('image')
        note = validated_data.get('note')
        
        doctor = CustomDoctor.objects.create_user(name=name, proffession=proffession, adresse=adresse,
          experience=experience, about=about,heure=heure, image=image)
        if doctor :
            doctor.jours.set(jours) 
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
       instance.heure= validated_data.get('heure', instance.heure)
       instance.image= validated_data.get('image', instance.image)
       instance.note= validated_data.get('note', instance.note)
       jours_ids = self.validated_data.get('jours', [])
       instance.jours.set(jours_ids)
       instance.save()
       return instance
# day where doctor is disponibles

class JourHopitalSerializer(serializers.ModelSerializer):
    class Meta():
        model = Jour_Doctor
        fields = '__all__'
class JourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jour_Doctor
        fields = '__all__'
    def create(self, validated_data):
        jour = validated_data.get('jour')
        heure_debut = validated_data.get('heure_debut')
        heure_fin = validated_data.get('heure_fin')
        jour= Jour_Doctor.objects.create_user(jour=jour,  heure_fin= heure_fin,heure_debut=heure_debut)
        return jour
class UpdateJourSerializer(serializers.ModelSerializer):
     class Meta():
        model = Jour_Doctor
        fields ='__all__'
     def update(self,instance,validated_data):
       instance.jour = validated_data.get('jour', instance.jour)
       instance.heure_debut= validated_data.get('heure_debut', instance.heure_debut)
       instance.heure_fin = validated_data.get('heure_fin', instance.heure_fin)
       instance.save()
       return instance