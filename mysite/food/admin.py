from django.contrib import admin

from .models import Photo

# Register your models here.
from .models import Place
class PhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Place)
