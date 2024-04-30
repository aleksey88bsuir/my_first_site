from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author}: {self.title} (опубликовано: {self.is_published})'


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
