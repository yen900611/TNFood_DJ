from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)
    style = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=20, help_text='Enter the name of store')
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, default="No phone number")
    web_site = models.CharField(max_length=200, default="No web site")
    introduction = models.CharField(max_length=100, default="不用問去吃就對了")
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag, through='Tag_Management', through_fields=('place', 'tags'))

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='photos')
    place = models.ForeignKey(Place, help_text="The place that this photo come from.", on_delete=models.SET_NULL,
                              null=True)


class Tag_Management(models.Model):
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)


class Device_Management(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    devices = models.ForeignKey(Device, on_delete=models.CASCADE)
