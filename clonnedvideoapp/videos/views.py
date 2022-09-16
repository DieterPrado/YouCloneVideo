from http.client import HTTPResponse
from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import User, Channel, Video, Comment
from django.views import generic
from django.utils import timezone
from .forms import RegisterForm, UploadVideoForm, PostCommentForm
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


@login_required
def profile(request, user_id):
    context = {
        "user": get_user_model().objects.get(pk = user_id),
        "videos": Video.objects.filter(author = user_id)
    }
    return render(request, "videos/profile.html", context)

@login_required
def upload(request):
    if request.method == "POST":
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return HttpResponseRedirect("/videos/")
    else:
        form = UploadVideoForm()
    return render(request, "videos/upload.html", {"form":form})


def watch(request, video_id):
    video = get_object_or_404(Video, pk = video_id)
    if request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.video = video
            comment.save()
    else:
        form = PostCommentForm()
    
    context = {
        "video": video,
        "form": form,
    }
    return render(request, "videos/watch.html", context)

    



class IndexView(generic.ListView):
    pass



class UserDetailView(generic.DetailView):
    model = User
    template_name = "videos/user_detail.html"
    context_object_name = "user_detail"

