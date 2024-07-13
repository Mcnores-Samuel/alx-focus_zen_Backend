#!/usr/bin/env python3
"""This module creates users and authenticates them."""
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from alxfocuszen_engine.api.v1.engine.user_serializer import UserProfileSerializer
from alxfocuszen_engine.models.user import UserProfile


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
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(res, status=status.HTTP_201_CREATED)
