from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):

    name=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    name=models.CharField(max_length=200)
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    description=models.TextField(null=True,blank=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    body=models.TextField()
    room=models.ForeignKey(Room,models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[0:50]