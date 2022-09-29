from django.contrib import admin

from .models import Photo, Place, Tag, Tag_Management, Device, Device_Management

admin.site.register(Photo, admin.ModelAdmin)
admin.site.register(Place, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(Tag_Management, admin.ModelAdmin)
admin.site.register(Device, admin.ModelAdmin)
admin.site.register(Device_Management, admin.ModelAdmin)
