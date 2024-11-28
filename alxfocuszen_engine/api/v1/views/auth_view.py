#!/usr/bin/env python3
"""This module creates users and authenticates them."""
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from alxfocuszen_engine.api.v1.engine.user_serializer import UserProfileSerializer
from alxfocuszen_engine.models.user import UserProfile
from django.utils import timezone


class SignUpView(generics.CreateAPIView):
    """This class creates a new user."""
    serializer_class = UserProfileSerializer

    def post(self, request):
        """This method creates a new user."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = UserProfile.objects.get(email=user_data['email'])
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token),
        refresh_token = str(refresh)

        payload = {
            'message': 'Account Successfully created',
            'username': user.username,
        }
        response = Response(payload, status=status.HTTP_201_CREATED)

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