from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.sessions.models import Session

from .models import Photo, Place, Tag, Device, Device_Management


class PhotoInlineAdmin(admin.TabularInline):
    model = Photo


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'web_site', 'updated_at','created_at')
    list_editable = ('name', 'address', 'web_site')
    list_filter = ('updated_at', 'tag')
    search_fields = ('name', 'address', 'web_site')
    ordering = ('-id',)
    readonly_fields = ('updated_at','created_at')
    inlines = [PhotoInlineAdmin]
    filter_horizontal = ('tag', 'devices',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'group')
    list_editable = ('name', 'value', 'group')
    list_filter = ('group',)
    search_fields = ('name', 'group')
    ordering = ('-id',)
    # readonly_fields = ('pub_date',)
    # inlines = [ PhotoInlineAdmin]
    # filter_horizontal = ('tag','devices',)

class SessionAdmin(ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Photo, admin.ModelAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Tag_Management, admin.ModelAdmin)
admin.site.register(Device, admin.ModelAdmin)
# admin.site.register(Device_Management, admin.ModelAdmin)
