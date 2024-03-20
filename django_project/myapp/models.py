from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
from base import settings
import os

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class animal(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    code = models.CharField(max_length=50,null=False)
    number = models.CharField(max_length=50,null=True,)
    date = models.DateField(null=False)
    image = models.ImageField(null=True, default='default.jpg')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,null=False,default='F')
    parent = models.CharField(max_length=100,null=True)
    
    
    def get_absolute_url(self):
        return reverse("viewrecord", args=[self.pk])
    
   

# class deceased(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     code = models.CharField(max_length=50,null=True)
#     number = models.CharField(max_length=50,null=True,)
#     date = models.DateField(null=True)
#     died = models.DateField(null=True,auto_now)
#     image = models.ImageField(null=True, default='default.jpg')
#     pass