from django.contrib.auth.models import User
from django.db import models

class Blogmodel(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='blog')
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

   
