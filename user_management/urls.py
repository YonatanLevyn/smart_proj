from django.urls import path
from .views import UserRegisterView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),  
    path('login/', views.login, name='login'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/<int:pk>/update_introduction/', views.update_introduction, name='update_introduction'),
    path('update_profile_photo/<int:pk>/', views.update_profile_photo, name='update_profile_photo'),
    path('update_cover_photo/<int:pk>/', views.update_cover_photo, name='update_cover_photo'),
]