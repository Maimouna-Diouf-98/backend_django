from django.urls import path
from .views import CreateDoctorAPI, JourEtHeure 

urlpatterns = [
    path('create-doctor/', CreateDoctorAPI.as_view(), name='create-doctor'),
    path('create-jour/', JourEtHeure.as_view(), name='create-jour'),
]