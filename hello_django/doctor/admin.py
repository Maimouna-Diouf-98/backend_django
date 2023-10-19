from django.contrib import admin

from .models import CustomDoctor,Jour_Doctor
# Register your models here.
admin.site.register(CustomDoctor)
admin.site.register(Jour_Doctor)

