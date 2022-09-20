from django.db import models

class Store(models.Model):
    store_name = models.CharField(max_length=20, help_text='Enter the name of store')
    address = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.store_name

