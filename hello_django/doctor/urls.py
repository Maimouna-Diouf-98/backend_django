from django.urls import path
from doctor import views

urlpatterns = [
    path('list-doctor/', views.doctors_list),
    path('create-doctor/', views.CreateDoctorAPI.as_view()),
    path('update-doctor/<int:pk>/',  views.UpdateDoctorAPI.as_view()),
    path('list-id-doctor/<int:pk>/',  views.list_id_doctor),
    path('delete-doctor/<int:pk>/',  views.delete_doctor),
]