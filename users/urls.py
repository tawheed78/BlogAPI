from django.urls import path, include
from .views import UserAPIView, NewTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', UserAPIView.as_view()),
    path('login/', NewTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]