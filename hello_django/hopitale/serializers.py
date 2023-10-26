from rest_framework import serializers
from .models import CustomHopitale,Specialist,Jour_hopitale

class JourSerializer(serializers.ModelSerializer):
    class Meta():
        model = Jour_hopitale
        fields = '__all__'
        # Specialist
class SpecialistSerializer(serializers.ModelSerializer):
    class Meta():
        model = Specialist
        fields = '__all__'

# create hopital 
class HopitalSerializer(serializers.ModelSerializer):
    jours = serializers.PrimaryKeyRelatedField(many=True, queryset=Jour_hopitale.objects.all())
    specialist =serializers.PrimaryKeyRelatedField(many=True, queryset=Specialist.objects.all())
    class Meta():
        model = CustomHopitale
        fields = '__all__'
