from django.test import TestCase
from django.utils import timezone
from .models import User, Video
from django.db import IntegrityError

def create_a_user(
    username = "johnnyexampleAwesome", 
    email = "john@example.com",
    name = "Johnny",
    last_name = "Example",
    ):
    return User.objects.create(username = username,
    email = email,
    name = name,
    last_name = last_name
    )
    

class UserModelTest(TestCase):
    def test_no_user_without_username_or_email(self):
        """
        Makes sure that no users can be registered without an email and username
        """
        pass

    def test_no_more_than_one_user_with_same_email(self):
        pass

    def test_no_more_than_one_user_with_same_username(self):
        pass


class CommentModelTest(TestCase):
    pass


class UserDetailViewTest(TestCase):
    pass


class VideoDetailViewTest(TestCase):
    def test_can_not_access_private_video(self):
        pass
    
    def test_video_can_not_be_published_in_the_future(self):
        pass

    def test_if_not_the_author_can_not_delete_video(self):
        pass





