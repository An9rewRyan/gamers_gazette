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
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    comments = models.IntegerField( default=0)

class Like(models.Model):

    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Dislike(models.Model):

    user = models.ForeignKey(User, related_name='dislikes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):

    texts = models.TextField()
    post = models.ForeignKey(Post,related_name='commentaris',on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_id = models.IntegerField(primary_key=True)
    pub_date = models.DateTimeField(auto_now=False)
    display = models.BooleanField(default=True)
    

    def __str__(self):
        return self.texts

class CommentChild(models.Model):

    texts = models.TextField()
    comment = models.ForeignKey(Comment, related_name='CommentChild',on_delete = models.CASCADE)
    prev = models.ForeignKey(Comment, related_name='ChildPrev',on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name ='comment_childs', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    child_id = models.IntegerField(primary_key=True)

class View(models.Model):

    user = models.ForeignKey(User, related_name='view', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

