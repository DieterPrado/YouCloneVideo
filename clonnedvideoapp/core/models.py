from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, )
    user_email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_birth_date = models.DateField("Users birth date")
    user_register_date = models.DateTimeField("Date user registered")
    user_last_joined_date = models.DateTimeField("Last time joined")

    def __str__(self):
        return self.username


class Channel(models.Model):
    channel_name = models.CharField(max_length=50, unique=True)
    channel_creation_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.channel_name


class Video(models.Model):
    video_file = models.FileField(upload_to="")
    video_name = models.CharField(max_length=200)
    video_description = models.TextField()
    user_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    channel_author = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.video_name

class Comment(models.Model):
    comment_text = models.TextField(max_length=1000)
    comment_post_date = models.DateTimeField()
    comment_is_edited = models.BooleanField()
    comment_likes = models.IntegerField()
    comment_dislikes = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reply = models.ForeignKey("self",on_delete=models.CASCADE) 

    def __str__(self):
        return "This is a comment"





