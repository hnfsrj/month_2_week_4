from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=100, unique=True)
    Content = models.TextField(max_length = 5000)
    Category = models.CharField(max_length = 100)
    Image = models.ImageField(null=True, blank=True)
    Tags = ArrayField(models.CharField(max_length = 100), blank=True, null=True)

    def __str__(self):
        return self.title
