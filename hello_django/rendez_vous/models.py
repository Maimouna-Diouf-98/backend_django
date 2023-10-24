from django.db import models

class CustomRendezVous(models.Model):
    # Choices pour la durée
    DURATION = [
        ('30 minutes', '30 minutes'),  # Ajusté la valeur pour correspondre au choix
        ('1 heure', '1 heure'),
        ('1 heure 30 minutes', '1 heure 30 minutes'),  # Ajusté la valeur
        ('2 heures', '2 heures'),  # Ajusté la valeur
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
        (20, '20'),  # Les valeurs numériques sont associées à des chaînes de caractères
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
    payment = models.CharField(max_length=50, choices=PAYMENT, default="Paypal")  # Corrigé la faute de frappe ici
    card_name = models.CharField(max_length=255, default="mai")
    card_number = models.IntegerField(default=23456)
    expiry_date = models.DateField(default='2023-10-10')
    cvv = models.IntegerField(default=3)
    save_to_database = models.BooleanField(default=False)  # Champs renommé pour éviter la collision de nom
    cash_payment = models.BooleanField(default=False)  # Champs renommé

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name_medecin
