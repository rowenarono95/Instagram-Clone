# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Post,Comment,Profile
import datetime as dt
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.wena = User.objects.create_user('wena', 'wena@gmail.com', '12345')
        self.profile = Profile(id=1,user=self.wena,bio="my bio")
        self.profile.save_profile()

    
        self.new_image= Post(id=1, image_name='image',description="wow",pub_date="20202-08-08",Author=self.joseph,author_profile=self.profile,likes="yes")
        self.new_image.save()
        
        # Creating a new comment and saving it
        self.comment = Comment(id=1,image=self.new_image,pub_date="08-08-2020",comment="wow",author=self.joseph)
        self.comment.save_comment()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Post))
        
    def test_save_method(self):
        self.new_image.save_image()
        new_image = Post.objects.all()      
        self.assertTrue(len(new_image) >0)
        
    def test_delete_image(self):
        self.new_image.delete_image()
        image = Post.objects.all()
        self.assertTrue(len(image)== 0)
        