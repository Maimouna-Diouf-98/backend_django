from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class DoctorManage (BaseUserManager):
    def create_user(**extra_fields):
        doctor = self.model(**extra_fields)
        doctor.save()
        return doctor

class CustomDoctor(AbstractBaseUser,PermissionsMixin):
      SEMAINE = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]

    name= models.CharField(max_length=255,)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    proffession= models.CharField(max_length=255,)
    adresse= models.CharField(max_length=255,null =True,blank=True)
    experience= models.CharField(max_length=255,null =True,blank=True)
    jours = models.ManyToManyField(SEMAINE)
    heure = models.TimeField()
    about= models.CharField(max_length=255,null =True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    objects = DoctorManage()
    
    def __str__(self):
     return self.name
class Heure(models.Model):
    heure = models.TimeField()

    def __str__(self):
        return self.heure.strftime('%H:%M')
class Jour(models.Model):
     SEMAINE = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]
    jours = models.ManyToManyField(SEMAINE)

    def __str__(self):
        return self.jours

class JourEtHeure(models.Model):
    jours = models.ForeignKey(Jour, on_delete=models.CASCADE)
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    modele = models.ForeignKey(CustomDoctor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.jour} as {self.heure} form {self.modele}"
