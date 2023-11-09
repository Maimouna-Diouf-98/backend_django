from django.db import models
from users.models import CustomUser
class CustomRendezVous(models.Model):
    # Choices pour la durée
    DURATION = [
        ('30 minutes', '30 minutes'),  
        ('1 heure', '1 heure'),
        ('1 heure 30 minutes', '1 heure 30 minutes'), 
        ('2 heures', '2 heures'),  
    ]
    
    # Choices pour le package
    PACKAGE = [
        ('Messaging', 'Messaging'),
        ('Voice Call', 'Voice Call'),
        ('Video Call', 'Video Call'),
        ('In Person', 'In Person'),
    ]

    # Choices pour le montant (amount)
    AMOUNT = [
        (20, '20'), 
        (40, '40'),
        (60, '60'),
        (100, '100'),
    ]
 
    # Choices pour la réservation (booking)
    BOOKING = [
        ('Self', 'Self'),
        ('Other', 'Other'),
    ]
    
    # Choices pour le genre (gender)
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    # Choices pour le paiement (payment)
    PAYMENT = [
        ('Paypal', 'Paypal'),
        ('Apple Pay', 'Apple Pay'),
    ]

    name_medecin = models.CharField(max_length=255, null=True, blank=True)
    profession_medecin = models.CharField(max_length=255, null=True, blank=True)
    adresse_medecin = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True, default='2023-10-10')
    heure = models.TimeField(default='00:00', null=True, blank=True)
    duree = models.CharField(max_length=50, choices=DURATION, default='30 minutes')
    package = models.CharField(max_length=50, choices=PACKAGE, default="Messaging")
    amount = models.IntegerField(choices=AMOUNT, default=20)
    booking = models.CharField(max_length=50, choices=BOOKING, default='Self')
    gender = models.CharField(max_length=50, choices=GENDER, default='Male')
    age = models.IntegerField(null=True, blank=True, default=10)
    probleme = models.CharField(null=True, blank=True, default='bonjour')
    payment = models.CharField(null=True, blank=True,max_length=50, choices=PAYMENT, default="") 
    # carte= models.ManyToManyField('Carte', blank=True)
    cash_payment = models.BooleanField(null=True, blank=True,default=False)  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name_medecin
class Carte(models.Model):
    card_name = models.CharField(null=True, blank=True, default="")
    card_number = models.IntegerField(null=True, blank=True,default=0)
    expiry_date = models.DateField(null=True, blank=True,default='YY-MM')
    cvv = models.IntegerField(null=True, blank=True,default=0)
    save_to_database = models.BooleanField(null=True, blank=True,default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
         if self.expiry_date:
           return self.expiry_date.strftime('%m-%y') 
         return self.card_name