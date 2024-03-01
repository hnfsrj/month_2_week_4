from django.db import models
from BlogApp.models import Post

# Create your models here.
class Comment(models.Model):
    Content = models.TextField()
    Author = models.CharField(max_length = 200)
    Published_date = models.DateTimeField()
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return self.Content[0:6]
