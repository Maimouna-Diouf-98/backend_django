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
    email = models.EmailField(max_length=250, unique=True)
    password= models.CharField(max_length=128,null =True)
    name= models.CharField(max_length=255,null =True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    agree= models.BooleanField(default=True)


    USERNAME_FIELD = 'email'

    objects = UserManage()
    
    def __str__(self):
     return self.email