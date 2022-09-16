from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


def get_current_date():
    return timezone.now()

class User(AbstractUser):
    is_private = models.BooleanField(default=False)


class Channel(models.Model):
    channel_name = models.CharField(max_length=50, unique=True)
    channel_creation_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.channel_name


class Video(models.Model):
    video_file = models.FileField(upload_to="videos")
    video_name = models.CharField(max_length=200)
    video_description = models.TextField()
    is_private = models.BooleanField(default=False, verbose_name="Is the video private?")
    post_date = models.DateTimeField(default=get_current_date)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_name

class Comment(models.Model):
    comment_text = models.TextField(max_length=1000)
    comment_post_date = models.DateTimeField(default=get_current_date)
    comment_is_edited = models.BooleanField(default=False)
    comment_likes = models.IntegerField(default=0)
    comment_dislikes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reply = models.ForeignKey("self",on_delete=models.CASCADE, null=True, blank= True) 

    def __str__(self):
        return "This is a comment"





