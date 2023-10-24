from django.db import models
# Create your models here.


class CustomDoctor(models.Model):
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
    jours = models.ManyToManyField('Jour_Doctor', related_name='doctors',blank=True)
    image = models.ImageField(upload_to='media',null=True,blank=True)
    note = models.FloatField(null=True,blank=True, default=0.0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    
    def __str__(self):
     return self.name


class Jour_Doctor(models.Model):
    jour = models.CharField(max_length=10, choices=CustomDoctor.SEMAINE)
    heure_debut = models.TimeField(default='00:00')
    heure_fin = models.TimeField(default='00:00')

    if heure_debut :
       def __str__(self):
        return self.heure_debut.strftime('%H:%M')
    
    if heure_fin :
       def __str__(self):
        return self.heure_fin.strftime('%H:%M')
    

    def __str__(self):
        return f"{self.jour} - De {self.heure_debut} à {self.heure_fin}"