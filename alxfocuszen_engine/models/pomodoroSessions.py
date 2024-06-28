from django.db import models
from django.core.exceptions import ValidationError
from alxfocuszen_engine.models.user import UserProfile
from alxfocuszen_engine.models.tasks import Task
from django.utils import timezone


class PomodoroSessionStatus(models.TextChoices):
    """This class defines the Pomodoro session status enumeration."""
    PENDING = 'pending', 'Pending'
    PAUSED = 'paused', 'Paused'
    IN_PROGRESS = 'in_progress', 'In Progress'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'


class PomodoroSession(models.Model):
    """The PomodoroSession model represents a single Pomodoro session
    completed by a user.

    Fields:
        user (ForeignKey): The user who completed the session.
        task (ForeignKey): The task associated with the session.
        start_time (DateTimeField): The timestamp when the session started.
        end_time (DateTimeField): The timestamp when the session ended.
        number_of_breaks (PositiveIntegerField): The number of breaks taken during the session.
        number_of_pomodoros (PositiveIntegerField): The number of Pomodoros completed during the session.
        pomodoro_length (PositiveIntegerField): The length of each Pomodoro in minutes.
        break_length (PositiveIntegerField): The length of each short break in minutes.
        long_break_length (PositiveIntegerField): The length of each long break in minutes.
        task_completed (BooleanField): Indicates whether the task was completed during the session.
        task_cancelled (BooleanField): Indicates whether the task was cancelled during the session.
        task_rescheduled (BooleanField): Indicates whether the task was rescheduled during the session.
        task_duration (DurationField): The total duration of the task.
        status (CharField): The current status of the session.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='pomodoro_sessions')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='pomodoro_sessions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    number_of_breaks = models.PositiveIntegerField(default=0)
    number_of_pomodoros = models.PositiveIntegerField(default=0)
    pomodoro_length = models.PositiveIntegerField(default=25)
    break_length = models.PositiveIntegerField(default=5)
    long_break_length = models.PositiveIntegerField(default=15)
    task_completed = models.BooleanField(default=False)
    task_cancelled = models.BooleanField(default=False)
    task_rescheduled = models.BooleanField(default=False)
    task_duration = models.DurationField(default=timezone.timedelta)
    status = models.CharField(
        max_length=20,
        choices=PomodoroSessionStatus.choices,
        default=PomodoroSessionStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """This method validates the PomodoroSession model instance."""
        if self.start_time >= self.end_time:
            raise ValidationError('The end time must be after the start time')
        # Check for overlapping sessions for the same user
        overlapping_sessions = PomodoroSession.objects.filter(
            user=self.user,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)
        if overlapping_sessions.exists():
            raise ValidationError('This session overlaps with another session for the same user.')

    def save(self, *args, **kwargs):
        """This method saves the PomodoroSession model instance."""
        self.full_clean()
        super().save(*args, **kwargs)

    def total_session_duration(self):
        """Returns the total duration of the session in minutes."""
        return (self.end_time - self.start_time).total_seconds() // 60

    def __str__(self):
        """This method returns a string representation of the PomodoroSession model instance."""
        return f'{self.user} - {self.task} - {self.start_time} - {self.end_time} - {self.status}'

    class Meta:
        """This class defines the metadata options for the PomodoroSession model."""
        verbose_name = 'Pomodoro Session'
        verbose_name_plural = 'Pomodoro Sessions'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'task', 'start_time', 'end_time']),
            models.Index(fields=['status']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'task', 'start_time', 'end_time'],
                                    name='unique_session_per_task')
        ]
