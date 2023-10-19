from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class DoctorManage (BaseUserManager):
    def create_user(self, **extra_fields):
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
    proffession= models.CharField(max_length=255,)
    adresse= models.CharField(max_length=255,null =True,blank=True)
    experience= models.IntegerField(default=0,null =True,blank=True)
    about= models.CharField(max_length=255, null=True,blank=True)
    jours = models.ManyToManyField('Jour_Doctor', related_name='doctors', blank=True)
    heure = models.TimeField(default='00:00:00')
    image = models.ImageField(upload_to='media',null=True,blank=True)
    note = models.FloatField(null=True,blank=True, default=0.0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_doctors',blank=True,editable=False)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_doctors',blank=True,editable=False)

    objects = DoctorManage()
    USERNAME_FIELD = 'name'
    
    if heure:
      def __str__(self):
        return self.heure.strftime('%H:%M')
    
    def __str__(self):
     return self.name


class Jour_Doctor(models.Model):
    jour = models.CharField(max_length=10, choices=CustomDoctor.SEMAINE)
    heure_debut = models.TimeField(default='00:00')
    heure_fin = models.TimeField(default='00:00')

    objects = DoctorManage()
    USERNAME_FIELD = 'jour'
    if heure_debut :
       def __str__(self):
        return self.heure_debut.strftime('%H:%M')
    
    if heure_fin :
       def __str__(self):
        return self.heure_fin.strftime('%H:%M')
    

    def __str__(self):
        return f"{self.jour} - De {self.heure_debut} à {self.heure_fin}"