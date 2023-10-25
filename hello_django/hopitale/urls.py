from django.urls import path
from hopitale import views

urlpatterns = [
    path('create-hopital/', views.HopitalAPI.as_view()),
    path('create-jour/', views.JourAPI.as_view()),
    path('create-specialist/', views.SpecialistAPI.as_view()),
    path('list_hopital/', views.hopital_list),
    path('list_jour/', views.jour_list),
    path('list_special/', views.special_list),
    path('list_id_hopital/<int:pk>/', views.list_id_hopital),
    path('list_id_jour/<int:pk>/', views.list_id_jour),
    path('list_id_specialist/<int:pk>/', views.list_id_special),
    path('update_hopital/<int:pk>/', views.update_hopital),
    path('update_jour/<int:pk>/', views.update_jour),
    path('update_special/<int:pk>/', views.update_special),
    path('delete_hopital/<int:pk>/', views.delete_hopital),
]