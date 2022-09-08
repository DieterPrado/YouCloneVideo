from django.shortcuts import render
from .models import User, Channel, Video, Comment
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    pass


class UserDetailView(generic.DetailView):
    model = User
    template_name = "videos/user_detail.html"
    context_object_name = "user_detail"
    

class ChannelDetailView(generic.DetailView):
    pass


class VideoDetailView(generic.DetailView):
    pass


class VideoUpload():
    pass

