from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated', 'author']
    prepopulated_fields = {'slug': ('title',)}

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'date_created', 'name_author']
