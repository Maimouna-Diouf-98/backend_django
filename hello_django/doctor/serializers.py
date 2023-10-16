from rest_framework import serializers
from .models import CustomDoctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta():
      model=CustomDoctor
      fields =('name',' proffession','adresse','experience','heure','about','jours')

class CreateDoctorSerializer(serializers.ModelSerializer):
   class Meta():
        model = CustomDoctor
        fields =('__all__')
        
