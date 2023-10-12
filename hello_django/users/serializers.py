from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomUser
        fields =('id','email','name','agree')

class  CreateUserSerializer(serializers.ModelSerializer):   
    class Meta():
        model = CustomUser
        fields =('__all__')
        extra_kwargs = {
            'password' :{
                'required':True,  
            },
              'name' :{
                'required':True,  
            },
           
        }
    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('utilisateur avec l\n email exist')
        return attrs
    def create(self,validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        name= validated_data.get('name')
        agree = validated_data.get('agree')
        user = CustomUser.objects.create_user(email=email, password=password,
         name=name,agree=agree)
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
     class Meta():
        model = CustomUser
        fields =('email','name','password','agree')  
     def update(self,instance,validated_data):
       instance.name = validated_data.get('name', instance.name)
       instance.agree = validated_data.get('agree', instance.agree)
       password = validated_data.get('password')
       if password:
           instance.set_password(password)
       instance.save()
       return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    
    def validate(self,  attrs,):
        email = attrs.get('email')
        password = attrs.get('password')
        if not email or not password:
            raise serializers.ValidationError("Please give both email and password.")

        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email does not exist.')
        user = authenticate(request=self.context.get('request'), email=email,password=password)
        if not user:
            raise serializers.ValidationError("Wrong Credentials.")
        attrs['user'] = user
        return attrs
  
