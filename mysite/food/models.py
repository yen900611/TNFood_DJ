from django.db import models

# Create your models here.

class Photo(models.Model):
    name=models.CharField(max_length=255)
    file=models.ImageField(upload_to='photos')
class Place(models.Model):
    name = models.CharField(max_length=20, help_text='Enter the name of store')
    address = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
