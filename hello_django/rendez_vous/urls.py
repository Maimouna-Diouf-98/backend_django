from django.urls import path
from rendez_vous import views

urlpatterns = [
    path('create_rendez_vous/', views.RendezVousAPI.as_view()),
    path('create_carte/', views.CarteAPI.as_view()),
    path('list_rendez_vous/', views.ListRendezVousAPI.as_view()),
    path('list_carte/', views.ListCarteAPI.as_view()),
    path('list_id_rendez_vous/<int:pk>/', views.list_id_rendez_vous),
    path('list_id_carte/<int:pk>/', views.list_id_carte),
    path('update_rendez_vous/<int:pk>/', views.list_update),
    path('update_carte/<int:pk>/', views.carte_update),
    path('delete_rendez_vous/<int:pk>/', views.delete_rendez_vous),
]