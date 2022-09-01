from django.urls import path
from . import views


app_name = "videos"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index" ),
    path('users/<int:user_id>', views.UserDetailView.as_view(), name="user_detail"),
    path('watch/<int:video_id>', views.VideoDetailView.as_view(), name="video_detail"),
]
