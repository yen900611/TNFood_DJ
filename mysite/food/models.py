from django.db import models

# Create your models here.

class Photo(models.Model):
    name=models.CharField(max_length=255)
    file=models.ImageField(upload_to='photos')