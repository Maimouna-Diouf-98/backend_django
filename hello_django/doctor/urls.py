from django.urls import path
from doctor import views

urlpatterns = [
  
    path('create_doctor/', views.CreateDoctorAPI.as_view()),
    path('create_jour/', views.JourAPI.as_view()),
    path('update_doctor/<int:pk>/',  views.update_doctor),
    path('update_jour/<int:pk>/',  views.update_jour),
    path('list_doctor/', views.doctors_list),
    path('list_jour/', views.jour_list),
    path('list_id_doctor/<int:pk>/',  views.list_id_doctor),
    path('list_id_jour/<int:pk>/',  views.list_id_jour),
    path('delete_doctor/<int:pk>/',  views.delete_doctor),
]