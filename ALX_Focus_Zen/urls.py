"""
URL configuration for ALX_Focus_Zen project.

The `urlpatterns` list routes URLs are alxfocuszen_engine api and the admin interface.
Additionally, the `urlpatterns` list also serves static files in development.
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from django.views.generic import RedirectView
from rest_framework import routers

urlpatterns = [
    path('alxfocuszen_engine/', include('alxfocuszen_engine.routes.urls')),
    path('', RedirectView.as_view(url='alxfocuszen_engine/')),
]
