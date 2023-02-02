from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BlogItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class BlogSetting(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=40)
    about_me = models.CharField(max_length=200)
    header_color = models.CharField(max_length=10)
    post_color = models.CharField(max_length=10)

    def __str__(self):
        return self.blog_name
