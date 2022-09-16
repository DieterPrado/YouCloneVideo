from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Video, Channel, Comment
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["video_name", "video_description", "is_private"]})
    ]
    inlines = [CommentInline]


admin.site.register(User, UserAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Channel)
admin.site.register(Comment)