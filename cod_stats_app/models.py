from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CodUser(AbstractUser):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    gamertag = models.CharField(max_length=150)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username}'