from django.db import models


# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=20, help_text='Enter the name of store')
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, default="No phone number")
    web_site = models.CharField(max_length=200, default="No web site")
    introduction = models.CharField(max_length=100, default="不用問去吃就對了")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='photos')
    place = models.ForeignKey(Place, help_text="The place that this photo come from.", on_delete=models.SET_NULL, null=True)
