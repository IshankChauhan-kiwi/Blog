from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'Profile')
    image = models.ImageField(upload_to= 'profile_picture', default='default.svg')

    def __str__(self):
        return f'{self.user}profile'


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, default="My Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return self.title +' | '+ str(self.author)

    def get_absolute_url(self):
        # return reverse('detail', args=(str(self.id)) )
        return reverse('index')
