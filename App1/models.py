from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

# Create your models here.
class Newuser(models.Model):
    Username = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    pwd = models.CharField(max_length=150)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=1)
    MartialStatus = models.CharField(max_length=15)