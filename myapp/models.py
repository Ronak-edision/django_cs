from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=100)
    detail=models.CharField(max_length=500)

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    message = models.TextField()
