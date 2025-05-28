from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=55, default='No title yet!')
    content = models.CharField(max_length=255, default='No content yet!')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at =  models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    pass