from django.db import models
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    image = models.URLField(max_length=200, null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()

# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)