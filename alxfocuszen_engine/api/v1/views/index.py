"""This is the index module for the alxfocuszen_engine app"""
from django.http import JsonResponse


def index(request):
    """This function returns a welcome message"""
    return JsonResponse({'message': 'Welcome to ALX Focus Zen!'})