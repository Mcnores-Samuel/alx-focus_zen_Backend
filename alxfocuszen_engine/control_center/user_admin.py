"""This module contains the UserProfile model admin view."""
from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
    """The UserProfileAdmin class defines the admin view for the UserProfile model.

    Args:
        admin (ModelAdmin): The base model admin class
    """
    list_display = ['email', 'username', 'is_active', 'is_superuser', 'created_at', 'updated_at']
    search_fields = ['email', 'username']
    list_filter = ['created_at', 'updated_at', 'is_active', 'is_staff', 'is_superuser']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']