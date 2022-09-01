from django.shortcuts import render
from .models import User, Channel, Video, Comment
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    pass


class UserDetailView(generic.DetailView):
    pass


class ChanelDetailView(generic.DetailView):
    pass


class VideoDetailView(generic.DetailView):
    pass

