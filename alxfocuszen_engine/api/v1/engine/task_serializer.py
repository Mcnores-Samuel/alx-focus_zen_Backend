#!/usr/bin/ env python3
"""This module contains the Task model serializer."""
from rest_framework import serializers
from alxfocuszen_engine.models.tasks import Task


class TaskSerializer(serializers.ModelSerializer):
    """The TaskSerializer class defines the serializer for the Task model."""
    class Meta:
        """This class defines the metadata for the TaskSerializer class."""
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'status': {'read_only': True}
        }