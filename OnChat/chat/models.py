from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name= models.CharField(max_length=1000)


class Message(models.Model):
    value= models.CharField(max_length=10000)
    date =models.DateTimeField(default= datetime.now, blank= True)
    # date =models.DateTimeField(auto_now_add=True,null=False)
    user= models.CharField(max_length=100)
    room= models.CharField(max_length=100)

