from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos')
    is_published = models.BooleanField(default=True)
