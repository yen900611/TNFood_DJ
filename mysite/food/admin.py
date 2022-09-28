from django.contrib import admin

from .models import Photo, Place, Tag, Tag_Management

admin.site.register(Photo, admin.ModelAdmin)
admin.site.register(Place,admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(Tag_Management, admin.ModelAdmin)
