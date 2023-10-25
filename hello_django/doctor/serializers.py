from rest_framework import serializers
from .models import CustomDoctor,Jour_Doctor
# creer le serialiser jour      
class JourSerializer(serializers.ModelSerializer):
    class Meta():
        model = Jour_Doctor
        fields = '__all__'
# doctor
class DoctorSerializer(serializers.ModelSerializer):
    jours = JourSerializer(many=True)
    class Meta():
      model=CustomDoctor
      fields ='__all__'
    def create(self, validated_data):
            jours_data = validated_data.get('jours', []) 

            doctor = CustomDoctor.objects.create(**validated_data)
            jours = [Jour.objects.get_or_create(nom=jour_data['nom'])[0] for jour_data in jours_data]
            doctor.jours.set(jours)

            return doctor