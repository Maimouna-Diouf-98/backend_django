from django.urls import path
from hopitale import views

urlpatterns = [
    path('create-hopital/', views.HopitalAPI.as_view()),
    path('create-jour/', views.JourAPI.as_view()),
    path('create-specialist/', views.SpecialistAPI.as_view()),
    path('list_hopital/', views.HopitalListView.as_view()),
    path('list_jour/', views.JourListView.as_view()),
    path('list_special/', views.SpecialListView.as_view()),
    path('list_id_hopital/<int:pk>/', views.list_id_hopital),
    path('list_id_jour/<int:pk>/', views.list_id_jour),
    path('list_id_specialist/<int:pk>/', views.list_id_special),
    path('update_hopital/<int:pk>/', views.HopitalUpdate.as_view()),
    path('update_jour/<int:pk>/', views.JourUpdate.as_view()),
    path('update_special/<int:pk>/', views.SpecialUpdate.as_view()),
    path('delete_hopital/<int:pk>/', views.delete_hopital),
]