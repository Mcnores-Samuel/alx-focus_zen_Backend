#!/usr/bin/ env python3
"""This module contains the PomodoroSession model serializer."""
from rest_framework import serializers
from alxfocuszen_engine.models.user import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """The UserProfileSerializer class defines the serializer for the UserProfile model."""
    class Meta:
        """This class defines the metadata for the UserProfileSerializer class."""
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'status': {'read_only': True}
        }