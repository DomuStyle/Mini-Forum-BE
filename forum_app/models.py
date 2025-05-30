from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=55, default='No title yet!')
    content = models.CharField(max_length=255, default='No content yet!')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"post {self.title} from {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    text = models.CharField(max_length=255, default='No comment text yet!')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_at =  models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.title} by {self.author}"