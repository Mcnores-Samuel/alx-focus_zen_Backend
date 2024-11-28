#!/usr/bin/env python3
"""This module creates users and authenticates them."""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from alxfocuszen_engine.models.user import UserProfile
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone


class SignUpView(APIView):
    """This class creates a new user."""
    def post(self, request, *args, **kwargs):
        """This method creates a new user."""
        data = request.data

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username or not password:
            raise ValidationError("Username and password are required")
        
        if UserProfile.objects.filter(username=username, email=email):
            raise ValidationError('Username already exists')
        
        user = UserProfile.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({
            'message': 'User created successfully',
            'username': username,
        }, status=status.HTTP_201_CREATED)

        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=True,
            samesite='Strict',
            max_age=300
        )
        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=True,
            samesite='Strict',
            max_age=timezone.timedelta(days=7).total_seconds()
        )

        return response