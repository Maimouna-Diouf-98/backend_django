from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,Group, Permission 
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class DoctorManage (BaseUserManager):
    def create_user(**extra_fields):
        doctor = self.model(**extra_fields)
        doctor.save()
        return doctor

class CustomDoctor(AbstractBaseUser,PermissionsMixin):
    name= models.CharField(max_length=255,)
    proffession= models.CharField(max_length=255,)
    adresse= models.CharField(max_length=255,null =True,blank=True)
    experience= models.CharField(max_length=255,null =True,blank=True)
    heure = models.TimeField()
    about= models.CharField(max_length=255,null =True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
#  permission 
    groups = models.ManyToManyField(Group, related_name='custom_doctors')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_doctors')

    objects = DoctorManage()
    
    def __str__(self):
     return self.name
 #  jour semaine
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
    
    jours = models.CharField(max_length=10, choices=SEMAINE)
    docteurs = models.ManyToManyField(CustomDoctor, related_name='jours_disponibles')

    def __str__(self):
        return self.jours
# heure

class Heure(models.Model):
    heure = models.TimeField()

    def __str__(self):
        return self.heure.strftime('%H:%M')

class JourEtHeure(models.Model):
    jours = models.ForeignKey(Jour, on_delete=models.CASCADE)
    heure = models.ForeignKey(Heure, on_delete=models.CASCADE)
    modele = models.ForeignKey(CustomDoctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.jours} à {self.heure} pour {self.modele}"   
