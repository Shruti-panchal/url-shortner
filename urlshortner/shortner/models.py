from django.db import models
from django.core.files import File


# Create your models here.

class url(models.Model):
    link= models.CharField(max_length=10000)
    uuid= models.CharField(max_length=10)