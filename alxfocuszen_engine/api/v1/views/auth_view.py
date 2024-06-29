#!/usr/bin/env python3
"""This module creates users and authenticates them."""
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from alxfocuszen_engine.models.user import UserProfile
from alxfocuszen_engine.api.v1.engine.user_serializer import UserProfileSerializer


class SignUpView(generics.CreateAPIView):
    """The SignUpView class creates new users.

    This class inherits from the CreateAPIView class in the generics module
    of the rest_framework package.

    Attributes:
        queryset: A queryset containing all user profiles.
        serializer: An instance of the UserProfileSerializer class.

    Methods:
        create: Creates a new user profile.
    """
    serializer = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        """This method creates a new user profile.

        The method takes a request object and optional arguments and keyword
        arguments. It creates a new user profile and returns a response
        object with the new user profile data and a status code.

        Args:
            request: An object containing the request data.
            *args: Optional arguments.
            **kwargs: Optional keyword arguments.

        Returns:
            A response object with the new user profile data and a status code.
        """
        serializer_class = UserProfileSerializer

        def create(self, request, *args, **kwargs):
            """This method creates a new user profile.

            The method takes a request object and optional arguments and keyword
            arguments. It creates a new user profile and returns a response
            object with the new user profile data and a status code.

            Args:
                request: An object containing the request data.
                *args: Optional arguments.
                **kwargs: Optional keyword arguments.

            Returns:
                A response object with the new user profile data and a status
                code.
            """
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)