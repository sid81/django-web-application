from distutils.command import upload
from unicodedata import name
from django.db import models

# Create your models here.

class Destination(models.Model):
    
    
    name = models.CharField(max_length=70)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)