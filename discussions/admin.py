from django.contrib import admin
from .models import Discussion


@admin.register(Discussion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}