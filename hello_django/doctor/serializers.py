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

 