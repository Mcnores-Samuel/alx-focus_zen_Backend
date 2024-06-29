"""This module contains the urls for the alxfocuszen_engine app"""
from django.urls import path
from alxfocuszen_engine.api.v1.views.index import index

urlpatterns = [
    path('', index, name='index'),
]