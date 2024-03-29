from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "birth_date"]
    

@admin.register(Book)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ["name", "get_authors"] # TODO разобраться как сделать verbose_name для метода get_authors
