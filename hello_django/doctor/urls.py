from django.urls import path
from doctor import views

urlpatterns = [
    # routes doctor
    path('create_doctor/', views.CreateDoctorAPI.as_view()),
    path('update_doctor/<int:pk>/',  views.DoctorDetail.as_view()),
    path('list_doctor/', views.DoctorListView.as_view()),
    path('list_id_doctor/<int:pk>/',  views.list_id_doctor),
    path('delete_doctor/<int:pk>/',  views.delete_doctor),
    # route jour
    path('create_jour/', views.JourAPI.as_view()),
    path('update_jour/<int:pk>/',  views.JourUpdateView.as_view()),
    path('list_jour/', views.JourListView.as_view()),
    path('list_id_jour/<int:pk>/',  views.list_id_jour),
]