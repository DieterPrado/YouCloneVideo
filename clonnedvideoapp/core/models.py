from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    join_date = models.DateTimeField("date joined")
    last_join_date = models.DateField("last time joined")

    def __str__(self):
        return self.username

class Video(models.Model):
    pass

class Reply(models.Model):
    reply_text = models.TextField(max_length=1000)
    author = models.OneToOneField

class Channel(models.Model):
    pass

