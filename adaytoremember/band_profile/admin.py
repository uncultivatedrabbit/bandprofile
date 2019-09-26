from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from .models import BandMember, Album, Song

class AdminSite(admin.ModelAdmin):
  AdminSite.site_header = "A Day to Remember"

class SongsInline(admin.TabularInline):
  model = Song


class AlbumAdmin(admin.ModelAdmin):
  inlines = [
    SongsInline
  ]

class SongAdmin(admin.ModelAdmin):
  ordering = ['onAlbum', 'trackNumber']

admin.site.register(BandMember)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)

