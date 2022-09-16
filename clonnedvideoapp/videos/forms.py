from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Video, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2", "email"]


class UploadVideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ["video_file", "video_name", "video_description","is_private"]
        exclude = ["author"]


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]