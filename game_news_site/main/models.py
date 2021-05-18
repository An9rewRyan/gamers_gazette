from django.db import models

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