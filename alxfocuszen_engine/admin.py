from alxfocuszen_engine.control_center.user_admin import UserProfileAdmin
from alxfocuszen_engine.control_center.tasks_admin import TasksAdmin
from alxfocuszen_engine.control_center.pomodoroSession_admin import PomodoroSessionAdmin
from alxfocuszen_engine.models.user import UserProfile
from alxfocuszen_engine.models.tasks import Task
from alxfocuszen_engine.models.pomodoroSessions import PomodoroSession
from django.contrib import admin

admin.site.site_title = 'ALX Focus Zen Admin'
admin.site.site_header = 'ALX Focus Zen Administration'
admin.site.index_title = 'Welcome to ALX Focus Zen Admin'
admin.site.index_title = 'Welcome to ALX Focus Zen Admin'


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Task, TasksAdmin)
admin.site.register(PomodoroSession, PomodoroSessionAdmin)