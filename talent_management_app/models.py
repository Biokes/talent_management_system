from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)

