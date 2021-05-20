from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):

    site = models.CharField(max_length=50, default="No title")
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField()
    pub_date = models.DateTimeField()
    img = models.ImageField(upload_to='images/', blank=True)
    post_id = models.IntegerField(primary_key=True)
    likes = models.IntegerField(default=0)

class Like(models.Model):

    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Dislike(models.Model):

    user = models.ForeignKey(User, related_name='dislikes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



