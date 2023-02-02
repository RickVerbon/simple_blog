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
