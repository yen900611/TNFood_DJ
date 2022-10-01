from django.contrib import admin

from .models import Photo, Place, Tag, Tag_Management, Device, Device_Management


class TagInlineAdmin(admin.StackedInline):
    model = Place.tags.through


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'web_site', 'pub_date')
    list_filter = ('pub_date', 'tags')
    search_fields = ('name', 'address', 'web_site')
    ordering = ('-id',)
    readonly_fields = ('pub_date',)
    inlines = [TagInlineAdmin, ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Photo, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
admin.site.register(Tag_Management, admin.ModelAdmin)
admin.site.register(Device, admin.ModelAdmin)
admin.site.register(Device_Management, admin.ModelAdmin)
