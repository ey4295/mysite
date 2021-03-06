from django.db import models

# Create your models here.
from django.utils import timezone
from froala_editor.fields import FroalaField


class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    introduction=models.TextField()
    content=FroalaField(options={
        'height': 800,
    })
    created_date=models.DateTimeField()

    def publish(self):
        self.created_date=timezone.now()
        self.save()

    def __str__(self):
        return (self.title)

class User_Request(models.Model):
    path=models.CharField(max_length=200);
    HTTP_REFERER=models.CharField(max_length=800);
    REMOTE_ADDR=models.CharField(max_length=50);
    VISIT_TIME=models.DateTimeField()
    def store(self):
        self.VISIT_TIME=timezone.now()
        self.save()
    def __str__(self):
        return (self.path)

class Message(models.Model):
    """
    message needed to be sent
    """
    content=models.CharField(max_length=2000)
    to_cell=models.CharField(max_length=20)
    current_time=models.DateTimeField()
    def store(self):
        self.current_time=timezone.now()
        self.save()
    def __str__(self):
        return (self.path)