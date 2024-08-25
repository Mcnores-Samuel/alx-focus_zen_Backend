#!/usr/bin/ env python3
"""This module contains the Task model serializer."""
from rest_framework import serializers
from alxfocuszen_engine.models.tasks import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    """The TaskSerializer class defines the serializer for the Task model."""
    class Meta:
        """This class defines the metadata for the TaskSerializer class."""
        model = Task
        fields = ['user', 'title', 'description', 'status', 'recurrence_type', 'recurrence_interval',
                  'days_of_week', 'days_of_month', 'time_of_day', 'due_date', 'priority',
                  'num_pomodoros', 'total_pomodoros', 'task_duration', 'task_theme_color',
                  'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'status': {'read_only': True}
        }

    def create(self, validated_data):
        """This method creates a new task."""
        task = Task.objects.create(**validated_data)
        return task
    
    def update(self, instance, validated_data):
        """This method updates an existing task."""
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.recurrence_type = validated_data.get('recurrence_type', instance.recurrence_type)
        instance.recurrence_interval = validated_data.get('recurrence_interval', instance.recurrence_interval)
        instance.days_of_week = validated_data.get('days_of_week', instance.days_of_week)
        instance.days_of_month = validated_data.get('days_of_month', instance.days_of_month)
        instance.time_of_day = validated_data.get('time_of_day', instance.time_of_day)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.num_pomodoros = validated_data.get('num_pomodoros', instance.num_pomodoros)
        instance.total_pomodoros = validated_data.get('total_pomodoros', instance.total_pomodoros)
        instance.task_duration = validated_data.get('task_duration', instance.task_duration)
        instance.task_theme_color = validated_data.get('task_theme_color', instance.task_theme_color)
        instance.updated_at = timezone.now()
        instance.save()
        return instance