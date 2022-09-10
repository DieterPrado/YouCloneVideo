from django.urls import path
from . import views


app_name = "videos"

urlpatterns = [
    path('', views.home, name="home" ),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),
    path('watch/<int:video_id>/', views.VideoDetailView.as_view(), name="video_detail"),
]
