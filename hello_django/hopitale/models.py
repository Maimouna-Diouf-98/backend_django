from django.db import models

class CustomHopitale(models.Model):
    SEMAINE = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]

    name = models.CharField(max_length=255, unique=True)
    specialist = models.ManyToManyField('Specialist', blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True)
    heure = models.TimeField(default='00:00')
    date = models.DateField()
    jours = models.ManyToManyField('Jour_hopitale', related_name='hospitals', blank=True)
    note = models.FloatField(null=True,blank=True, default=0.0)
    image = models.ImageField(upload_to='hopital', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    if heure:
      def __str__(self):
        return self.heure.strftime('%H:%M')
    

    def __str__(self):
        return self.name

class Jour_hopitale(models.Model):
    jour = models.CharField(max_length=10, choices=CustomHopitale.SEMAINE)
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

class Specialist(models.Model):
  specialist = models.CharField(max_length=255)
  def __str__(self):
        return self.specialist