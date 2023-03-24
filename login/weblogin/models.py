from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class registion(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=15)
    

# class User(AbstractUser):
#     adress=models.