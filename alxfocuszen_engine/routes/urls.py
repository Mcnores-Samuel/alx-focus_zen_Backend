"""This module contains the urls for the alxfocuszen_engine app"""
from django.urls import path
from alxfocuszen_engine.api.v1.views.auth_view import SignUpView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('api/v1/signup/', SignUpView.as_view(), name='signup'),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='refresh')
]