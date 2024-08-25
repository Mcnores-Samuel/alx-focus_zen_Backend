"""This module contains the UserProfile model admin view."""
from django.contrib import admin


class PomodoroSessionAdmin(admin.ModelAdmin):
    """The UserProfileAdmin class defines the
    admin view for the UserProfile model.

    Args:
        admin (ModelAdmin): The base model admin class
    """
    list_display = ['user', 'status', 'start_time', 'end_time', 'created_at', 'updated_at']
    search_fields = ['user', 'status']
    list_filter = ['created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    list_per_page = 50
    list_max_show_all = 100