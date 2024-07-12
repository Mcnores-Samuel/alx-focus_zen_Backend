#!/usr/bin/ env python3
"""This module contains the PomodoroSession model serializer."""
from rest_framework import serializers
from alxfocuszen_engine.models.user import UserProfile
from django.utils import timezone


class UserProfileSerializer(serializers.ModelSerializer):
    """The UserProfileSerializer class defines the serializer for the UserProfile model.
    It serializes the user data to be returned in the API response.

    Args:
        serializers (ModelSerializer): The base model serializer class
    """
    class Meta:
        """This class defines the metadata for the UserProfileSerializer class."""
        model = UserProfile
        fields = ['id', 'email', 'username', 'password', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        """This method creates a new user profile.

        Args:
            validated_data (dict): The validated user data
        
        Returns:
            UserProfile: The created user profile
        """
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        user = UserProfile.objects.get(email=validated_data['email'])
        return user