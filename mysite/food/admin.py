from django.contrib import admin

from .models import Photo, Place, Tag, Device, Device_Management


class PhotoInlineAdmin(admin.TabularInline):
    model = Photo


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'web_site', 'pub_date')
    list_editable = ('name', 'address', 'web_site')
    list_filter = ('pub_date', 'tag')
    search_fields = ('name', 'address', 'web_site')
    ordering = ('-id',)
    readonly_fields = ('pub_date',)
    inlines = [ PhotoInlineAdmin]
    filter_horizontal = ('tag','devices',)



admin.site.register(Place, PlaceAdmin)
admin.site.register(Photo, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
# admin.site.register(Tag_Management, admin.ModelAdmin)
admin.site.register(Device, admin.ModelAdmin)
# admin.site.register(Device_Management, admin.ModelAdmin)
