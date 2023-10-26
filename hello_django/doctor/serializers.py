from rest_framework import serializers
from .models import CustomDoctor,Jour_Doctor
# creer le serialiser jour      
class JourSerializer(serializers.ModelSerializer):
    class Meta():
        model = Jour_Doctor
        fields = '__all__'
# doctor serializer with get Id jour 
class DoctorSerializer(serializers.ModelSerializer):
    jours = serializers.PrimaryKeyRelatedField(many=True, queryset=Jour_Doctor.objects.all())
    class Meta():
        model=CustomDoctor
        fields ='__all__'
#  doctor serialier witt get id jour and propreter
class DoctorListSerializer(serializers.ModelSerializer):
    jours = JourSerializer(many=True)
    class Meta():
        model=CustomDoctor
        fields ='__all__'
 
 