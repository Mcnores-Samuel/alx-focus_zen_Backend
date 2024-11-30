"""This module contains the urls for the alxfocuszen_engine app"""
from django.urls import path
from alxfocuszen_engine.api.v1.views.auth_view import SignUpView
from alxfocuszen_engine.api.v1.views.obtainToken import CustomTokenObtainPairView
from alxfocuszen_engine.api.v1.views.refreshToken import CustomTokenRefreshView
from alxfocuszen_engine.api.v1.views.tasks_view import TaskListView
from alxfocuszen_engine.api.v1.views.verifyToken import CustomTokenVerifyView


urlpatterns = [
    path('api/v1/signup/', SignUpView.as_view(), name='signup'),
    path('api/v1/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/v1/refresh/', CustomTokenRefreshView.as_view(), name='refresh'),
    path('api/v1/token_verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/tasks/create/', TaskListView.as_view(), name='create_task'),
    path('api/v1/tasks/', TaskListView.as_view(), name='list_tasks'),
    path('api/v1/tasks/<int:pk>/', TaskListView.as_view(), name='update_task'),
    path('api/v1/tasks/<int:pk>/delete/', TaskListView.as_view(), name='delete_task'),
    path('api/v1/tasks/<int:pk>/complete/', TaskListView.as_view(), name='complete_task'),
    path('api/v1/tasks/<int:pk>/incomplete/', TaskListView.as_view(), name='incomplete_task'),
    path('api/v1/tasks/<int:pk>/archive/', TaskListView.as_view(), name='archive_task'),
    path('api/v1/tasks/<int:pk>/unarchive/', TaskListView.as_view(), name='unarchive_task'),
    path('api/v1/tasks/<int:pk>/star/', TaskListView.as_view(), name='star_task'),
    path('api/v1/tasks/<int:pk>/unstar/', TaskListView.as_view(), name='unstar_task'),
    path('api/v1/tasks/<int:pk>/priority/', TaskListView.as_view(), name='priority_task'),
    path('api/v1/tasks/<int:pk>/unpriority/', TaskListView.as_view(), name='unpriority_task'),
]