from rest_framework import serializers
from .models import CustomRendezVous


class RendezVousSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomRendezVous
        fields = '__all__'
