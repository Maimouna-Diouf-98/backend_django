from django.contrib import admin

from .models import CustomHopitale,Jour_hopitale,Specialist
# Register your models here.
admin.site.register(CustomHopitale)
admin.site.register(Jour_hopitale)
admin.site.register(Specialist)
