from django.urls import path
from . import views


urlpatterns = [
    path('create-user/', views.CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPI.as_view()),
]