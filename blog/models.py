from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    introduction=models.TextField()
    content=models.TextField()
    created_date=models.DateTimeField()

    def publish(self):
        self.created_date=timezone.now()
        self.save()

    def __str__(self):
        return (self.title)
