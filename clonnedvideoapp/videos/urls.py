from unicodedata import name
from django.urls import path
from . import views


app_name = "videos"

urlpatterns = [
    path('', views.home, name="home" ),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
    path('upload/', views.upload, name="video_upload"),
    path('watch/<int:video_id>/', views.watch, name="watch_video"),
]
