"""This module contains the urls for the alxfocuszen_engine app"""
from django.urls import path
from alxfocuszen_engine.api.v1.views.auth_view import SignUpView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from alxfocuszen_engine.api.v1.views.tasks_view import TaskListView


urlpatterns = [
    path('api/v1/signup/', SignUpView.as_view(), name='signup'),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/tasks/create/', TaskListView.as_view(), name='create_task'),
]