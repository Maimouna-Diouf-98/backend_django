from django.urls import path
from rendez_vous import views

urlpatterns = [
    path('create_rendez_vous/', views.RendezVousAPI.as_view()),
    path('list_rendez_vous/', views.ListRendezVousAPI.as_view()),
    path('list_id_rendez_vous/<int:pk>/', views.list_id_rendez_vous),
    # path('create-jour/', views.JourAPI.as_view()),
    # path('list_hopital/', views.hopital_list),
    # path('list_jour/', views.jour_list),
    # path('list_id_hopital/<int:pk>/', views.list_id_hopital),
    # path('list_id_jour/<int:pk>/', views.list_id_jour),
    # path('update_hopital/<int:pk>/', views.UpdateHopitalAPI.as_view()),
    # path('update_jour/<int:pk>/', views.UpdateJourAPI.as_view()),
    # path('delete_hopital/<int:pk>/', views.delete_hopital),
]