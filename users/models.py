from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add additional fields as per your requirements
#     phone_number = models.CharField(max_length=20)
#     date_of_birth = models.DateField()