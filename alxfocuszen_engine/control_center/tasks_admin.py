"""This module contains the UserProfile model admin view."""
from django.contrib import admin


class TasksAdmin(admin.ModelAdmin):
    """The UserProfileAdmin class defines the admin view for the UserProfile model.

    Args:
        admin (ModelAdmin): The base model admin class
    """
    list_display = ['title', 'status', 'recurrence_type', 'due_date', 'priority', 'created_at', 'updated_at']
    search_fields = ['title', 'status']
    list_filter = ['created_at', 'updated_at', 'status', 'recurrence_type', 'priority']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    list_per_page = 50
    list_max_show_all = 100