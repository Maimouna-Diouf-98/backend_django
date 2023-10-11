from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class UserManage (BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("l'email n'est pas dionnee")
        email=self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active= True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if not extra_fields.get('is_staff'):
           raise ValueError("superUser doit avoir is_staff=True")
        if not extra_fields.get('is_superuser'):
           raise ValueError("superUser doit avoir is_superuser=True")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    GENDER_CHOICES = {
        (1, 'male'),
        (2, 'female'),
        (3, 'others')
    }
    email = models.EmailField(max_length=250, unique=True)
    password= models.CharField(max_length=128,null =True)
    first_name= models.CharField(max_length=255,null =True,blank=True)
    last_name= models.CharField(max_length=255,null =True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, null= True)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    objects = UserManage()
    
    def __str__(self):
     return self.email