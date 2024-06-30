#!/usr/bin/env python3
"""This module creates users and authenticates them."""
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from alxfocuszen_engine.api.v1.engine.user_serializer import UserProfileSerializer


class SignUpView(generics.CreateAPIView):
    """This class creates a new user.
    The user data is validated and saved to the database.
    The user is then authenticated and tokens are generated.

    Args:
        generics (CreateAPIView): A generic class for creating a new user.

    Returns:
        Response: A response with the user data and tokens.
    """
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        """Create a new user and generate tokens.

        Args:
            request (Request): The request object.

        Returns:
            Response: A response with the user data and tokens.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)