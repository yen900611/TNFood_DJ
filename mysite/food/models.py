from django.core.exceptions import ValidationError
from django.db import models
from django_resized import ResizedImageField


# Create your models here.
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=10)
    value = models.CharField(max_length=30, default="None")
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
    tag = models.ManyToManyField(Tag,blank=True)
    devices = models.ManyToManyField(Device,blank=True)
    def __str__(self):
        return self.name

    def get_sample_by_order(self):
        if self.photo_set.count():
            return self.photo_set.first().file

def validate_file_size(value):
    filesize = value.size
    if filesize > 10240:
        raise ValidationError("The maximum file size that can be uploaded is 10KB")
    else:
        return value


class Photo(models.Model):
    name = models.CharField(max_length=255)
    file = ResizedImageField(size=[400, 400], crop=['middle', 'center'], force_format='PNG', upload_to='photos', validators=[validate_file_size])
    place = models.ForeignKey(Place, help_text="The place that this photo come from.", on_delete=models.SET_NULL,
                              null=True)


# 網站總訪問次數
# class VisitNumber(models.Model):
#     count = models.IntegerField(verbose_name='網站訪問總次數', default=0)  # 網站訪問總次數
#
#     class Meta:
#         verbose_name = '網站訪問總次數'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.count)
#
#
# # 單日訪問量統計
# class DayNumber(models.Model):
#     day = models.DateField(verbose_name='日期', default=timezone.now)
#     count = models.IntegerField(verbose_name='網站訪問次數', default=0)  # 網站訪問總次數
#
#     class Meta:
#         verbose_name = '網站日訪問量統計'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.day)


class Device_Management(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    devices = models.ForeignKey(Device, on_delete=models.CASCADE)
