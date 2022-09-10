import email
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User, Channel, Video, Comment
from django.views import generic
from django.utils import timezone
from .forms import RegisterForm
#from django.contrib.auth import views


def home(request):
    return render(request, "videos/home.html",{"message":"nothingimportant"})

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login")
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html",{"form": form}) 


class IndexView(generic.ListView):
    pass


class UserDetailView(generic.DetailView):
    model = User
    template_name = "videos/user_detail.html"
    context_object_name = "user_detail"

#class UserLoginView(generic.Logi)


class ChannelDetailView(generic.DetailView):
    pass


class VideoDetailView(generic.DetailView):
    pass


class VideoUpload():
    pass

