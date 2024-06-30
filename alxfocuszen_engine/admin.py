from alxfocuszen_engine.contral_center.user_admin import UserProfileAdmin
from alxfocuszen_engine.models.user import UserProfile
from django.contrib import admin

admin.site.site_title = 'ALX Focus Zen Admin'
admin.site.site_header = 'ALX Focus Zen Administration'
admin.site.index_title = 'Welcome to ALX Focus Zen Admin'
admin.site.index_title = 'Welcome to ALX Focus Zen Admin'


admin.site.register(UserProfile, UserProfileAdmin)