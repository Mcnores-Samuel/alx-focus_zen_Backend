"""This module contains the Task model class and the TaskStatus enumeration."""
from django.db import models
from django.core.exceptions import ValidationError
from alxfocuszen_engine.models.user import UserProfile
from django.utils import timezone


class TaskStatus(models.TextChoices):
    """This class defines the task status enumeration."""
    PENDING = 'pending', 'Pending'
    IN_PROGRESS = 'in_progress', 'In Progress'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'


class TaskRecurrenceType(models.TextChoices):
    """This class defines the task recurrence type enumeration."""
    NONE = 'none', 'None'
    DAILY = 'daily', 'Daily'
    WEEKLY = 'weekly', 'Weekly'
    MONTHLY = 'monthly', 'Monthly'
    YEARLY = 'yearly', 'Yearly'
    CUSTOM = 'custom', 'Custom'


class TaskPriority(models.IntegerChoices):
    """This class defines the task priority enumeration."""
    LOW = 1, 'Low'
    MEDIUM = 2, 'Medium'
    HIGH = 3, 'High'
    URGENT = 4, 'Urgent'


class Task(models.Model):
    """The Task model represents a task that needs to be completed.

    Fields:
        title (CharField): The title of the task.
        description (TextField): The detailed description of the task.
        status (CharField): The current status of the task.
        recurrence_type (CharField): The recurrence pattern of the task.
        recurrence_interval (PositiveIntegerField): The interval for custom recurrence.
        days_of_week (JSONField): Days of the week the task recurs.
        days_of_month (JSONField): Days of the month the task recurs.
        time_of_day (TimeField): Specific time of day for the task.
        due_date (DateField): The due date of the task.
        priority (PositiveIntegerField): The priority level of the task.
        created_at (DateTimeField): The timestamp when the task was created.
        updated_at (DateTimeField): The timestamp when the task was last updated.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING
    )
    recurrence_type = models.CharField(
        max_length=20,
        choices=TaskRecurrenceType.choices,
        default=TaskRecurrenceType.NONE
    )
    recurrence_interval = models.PositiveIntegerField(default=1)
    days_of_week = models.JSONField(default=list, blank=True, null=True)
    days_of_month = models.JSONField(default=list, blank=True, null=True)
    time_of_day = models.TimeField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.PositiveIntegerField(
        default=TaskPriority.MEDIUM,
        choices=TaskPriority.choices
    )
    num_pomodoros = models.PositiveIntegerField(default=0)
    total_pomodoros = models.PositiveIntegerField(default=0)
    task_duration = models.DurationField(null=True, blank=True)
    task_theme_color = models.CharField(max_length=7, default='#007bff')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """Validate the task fields."""
        if (self.recurrence_type == TaskRecurrenceType.CUSTOM and
            not (self.days_of_week or self.days_of_month)):
            raise ValidationError(
                'For custom recurrence, you must specify either days of the week or days of the month.')
        if self.recurrence_type == TaskRecurrenceType.NONE:
            self.recurrence_interval = 1
            self.days_of_week = []
            self.days_of_month = []
        if (self.recurrence_type in
            [TaskRecurrenceType.DAILY, TaskRecurrenceType.NONE] and self.time_of_day is None):
            raise ValidationError('Time of day is required for daily or non-recurrent tasks.')

    def save(self, *args, **kwargs):
        """Override save method to include validation logic."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['priority']),
            models.Index(fields=['due_date']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'title', 'due_date'], name='unique_task')
        ]
