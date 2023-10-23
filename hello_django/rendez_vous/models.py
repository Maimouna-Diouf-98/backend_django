from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class Rendez_VousManage(BaseUserManager):
    def create_user(self, **extra_fields):
        rendez_vous = self.model(**extra_fields)
        rendez_vous.save()
        return rendez_vous


class Custom_Rendez_Vous(AbstractBaseUser, PermissionsMixin):
    DURATION =[
       ('30 minute','30 minute'),
       ('1 heure', '1 heure'),
       ('1 heure 30 minute', '1h 30 minute'),
       ('2 heure', '2 heure'),
    ]
    PACKAGE = [
        ('Messaging', 'Messaging'),
        ('Voice Call', 'Voice Call'),
        ('Video Call', 'Video Call'),
        ('In Person', 'In Person'),
    ]
    AMOUNT = [
        (20, 20),
        (40, 40),
        (60, 60),
        (100, 100)
    ]
 
    BOOKING =[
        ('Self','Self'),
        ('Other','Other'),
    ]
    GENDER =[
        ('Male','Male'),
        ('Female','Female'),
    ]
    PAYEMENT =[
        ('Paypal','Paypal'),
        ('Apple Pay','Apple Pay'),
    ]
    name_medecin = models.CharField(max_length=255,null=True,blank=True)
    profession_medecin = models.CharField(max_length=255,null=True,blank=True)
    adresse_medcin = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    heure = models.TimeField(default='00:00',null=True,blank=True,)
    duree = models.CharField(max_length=50, choices=DURATION)
    package = models.CharField(max_length=50, choices=PACKAGE)
    amount = models.IntegerField(choices=AMOUNT)
    booking = models.CharField(max_length=50, choices=BOOKING)
    gender = models.CharField(max_length=50, choices=GENDER)
    age = models.IntegerField(null=True,blank=True,)
    probleme =models.CharField(max_length=255, null=True, blank=True)
    payement = models.CharField(max_length=50, choices=PAYEMENT)
    card_name = models.CharField(max_length=255)
    card_number = models.IntegerField(unique=True)
    expiry_date = models.DateTimeField()
    cvv =  models.IntegerField(unique=True)
    save = models.BooleanField(default=True)
    cash = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_rendez_vous', blank=True, editable=False)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_rendez_vous', blank=True, editable=False)

    objects=Rendez_VousManage()
    USERNAME_FIELD = 'name'
    if heure:
      def __str__(self):
        return self.heure.strftime('%H:%M')
    

    def __str__(self):
        return self.name



