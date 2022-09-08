from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Video, Channel, Comment
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Video)
admin.site.register(Channel)
admin.site.register(Comment)