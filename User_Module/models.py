from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserModel(AbstractUser):
    """
    The User model is used to store information about users.
    """
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
