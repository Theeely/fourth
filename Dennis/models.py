from django.db import models
from teluskolearn.models import User
# Creat   your models here.


class Topic(models.Model):
    name=models.CharField(max_length=200) 
    
    def __str__(self):
        return self.name
    
     
class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    name=models.CharField(max_length=50)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    desc=models.TextField(blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    def shortendesc(self):
        return self.desc[:100]+"..."
    
    class Meta:
        ordering=['-date_modified','-date_created']


    
class Message(models.Model):
     user=models.ForeignKey( User,on_delete=models.CASCADE,null=True)
     room=models.ForeignKey(Room,on_delete=models.CASCADE)
     body=models.TextField()
     date_created=models.DateTimeField(auto_now_add=True)
     date_modified=models.DateTimeField(auto_now=True)
     
     
     def __str__(self):
         return self.body[:100]
     
     def Shortenmessage(self):
         return self.body[:80]
     
    