from django.urls import path
from doctor import views

urlpatterns = [
    path('list-doctor/', views.doctors_list),
    path('create-doctor/', views.CreateDoctorAPI.as_view()),
    # path('list-doctor/', ListDoctor.as_view(), name='list-doctor'),
    # path('update-doctor/<int:pk>/',  UpdateDoctorAPI.as_view(), name='update-doctor'),
    # path('create-jour/', Jour.as_view(), name='create-jour'),
    # path('create-heure/', Heure.as_view(), name='create-heure'),
    # path('create-jour-heure/', JourEtHeure.as_view(), name='create-jour-heure'),
]