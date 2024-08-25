#!/usr/bin/env python3
"""This module contains the PomodoroSession model serializer."""
from rest_framework import serializers
from alxfocuszen_engine.models.pomodoroSessions import PomodoroSession
from django.utils import timezone


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

    def create(self, validated_data):
        """This method creates a new PomodoroSession."""
        session = PomodoroSession.objects.create(**validated_data)
        return session
    
    def update(self, instance, validated_data):
        """This method updates an existing PomodoroSession."""
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.number_of_breaks = validated_data.get('number_of_breaks', instance.number_of_breaks)
        instance.number_of_pomodoros = validated_data.get('number_of_pomodoros', instance.number_of_pomodoros)
        instance.pomodoro_length = validated_data.get('pomodoro_length', instance.pomodoro_length)
        instance.break_length = validated_data.get('break_length', instance.break_length)
        instance.break_interval = validated_data.get('break_interval', instance.break_interval)
        instance.start_break = validated_data.get('start_break', instance.start_break)
        instance.end_break = validated_data.get('end_break', instance.end_break)
        instance.task_completed = validated_data.get('task_completed', instance.task_completed)
        instance.task_cancelled = validated_data.get('task_cancelled', instance.task_cancelled)
        instance.task_rescheduled = validated_data.get('task_rescheduled', instance.task_rescheduled)
        instance.task_duration = validated_data.get('task_duration', instance.task_duration)
        instance.status = validated_data.get('status', instance.status)
        instance.updated_at = timezone.now()
        instance.save()
        return instance