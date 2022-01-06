from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
# profile_picture = models.ImageField(default='default-avatar.png', upload_to='pics', null=True, blank=True)
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

    def __str__(self):
        return self.title +' | '+ str(self.author)

    def get_absolute_url(self):
        # return reverse('detail', args=(str(self.id)) )
        return reverse('index')
