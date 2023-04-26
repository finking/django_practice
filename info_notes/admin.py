from django.contrib import admin

from .models import Sites, Nick, Notes


@admin.register(Sites)
class SitesAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'date_added']
    #prepopulated_fields = {"slug": ("name",)}


@admin.register(Nick)
class NickAdmin(admin.ModelAdmin):
    list_display = ['name', 'personal_website', 'picture']
    #prepopulated_fields = {"slug": ("name",)}


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']  #'slug'
    prepopulated_fields = {"slug": ("title",)}
