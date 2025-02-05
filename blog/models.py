from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
