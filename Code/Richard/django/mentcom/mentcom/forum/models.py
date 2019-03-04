from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=1000)
    url = models.CharField(max_length=500)
    byline = models.CharField(max_length=200)
    published_date = models.DateField()
    abstract = models.CharField(max_length=2500)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=10000)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='posts')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField(max_length=10000)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    # parent = models.ForeignKey(Comment)


