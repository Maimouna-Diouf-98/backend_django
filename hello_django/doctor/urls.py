from django.urls import path
from . import views


urlpatterns = [
    path('doctor-list', views.DoctorList),
    path('create-doctor/', views.CreateDoctor),
 
]