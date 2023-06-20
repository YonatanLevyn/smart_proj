from django.urls import path, include
from .views import UserViewSet, LogoutView, ProfileView, UpdateIntroductionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),  
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/update_introduction/', UpdateIntroductionView.as_view(), name='update_introduction'),
    path('api/', include(router.urls)), 
]
