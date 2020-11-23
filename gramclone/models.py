# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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
    image = models.ImageField(upload_to='new_post/', blank=True ,default = 'default.jpg')
    title = models.CharField(max_length=30, default='')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    caption = models.TextField(max_length=300)


    def __str__(self):
        return self.title

    def save_post(self):
        self.save()


class Comment(models.Model):
    image = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE,related_name='comment')
    comment_title = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    comment= models.TextField()

    def save_comment(self):
        self.save()

        
    def delete_comment(self):
        self.delete()

