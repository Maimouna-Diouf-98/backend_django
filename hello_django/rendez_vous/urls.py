from django.urls import path
from rendez_vous import views

urlpatterns = [
    path('create_rendez_vous/', views.RendezVousAPI.as_view()),
    path('list_rendez_vous/', views.ListRendezVousAPI.as_view()),
    path('list_id_rendez_vous/<int:pk>/', views.list_id_rendez_vous),
    path('update_rendez_vous/<int:pk>/', views.list_update),
    path('delete_rendez_vous/<int:pk>/', views.delete_rendez_vous),
]