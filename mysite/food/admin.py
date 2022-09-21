from django.contrib import admin

from .models import Photo

# Register your models here.
from .models import Place

admin.site.register(Photo, admin.ModelAdmin)
admin.site.register(Place,admin.ModelAdmin)
