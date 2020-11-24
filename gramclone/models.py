# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField()
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()


class Post(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=30, default='')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    caption = models.TextField(max_length=300)
    


    def __str__(self):
        return self.title

    def save_post(self):
        self.save()


class Comments(models.Model):
    image = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.content)

    def vaild(self):
        self.vaild = True
        self.save()