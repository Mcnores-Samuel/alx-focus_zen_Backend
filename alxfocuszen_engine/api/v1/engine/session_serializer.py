#!/usr/bin/env python3
"""This module contains the PomodoroSession model serializer."""
from rest_framework import serializers
from alxfocuszen_engine.models.pomodoroSessions import PomodoroSession


class PomodoroSessionSerializer(serializers.ModelSerializer):
    """The PomodoroSessionSerializer class defines the serializer for
    the PomodoroSession model.
    """
    class Meta:
        """This class defines the metadata for the PomodoroSessionSerializer class."""
        model = PomodoroSession
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'status': {'read_only': True}
        }