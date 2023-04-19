from django.contrib import admin
from galery.models import Photos

class PhotosList(admin.ModelAdmin):
    list_display = ("id", "name", "subtittle")
    list_display_links = ("id", "name")
    search_fields = ("name",)

admin.site.register(Photos, PhotosList)