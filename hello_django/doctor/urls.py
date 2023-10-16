from django.urls import path
from . import views


urlpatterns = [
    path('create-doctor/',  CreateDoctorAPI.as_view()),
    path('create-jour/',  JourEtHeure.as_view()),
 
]