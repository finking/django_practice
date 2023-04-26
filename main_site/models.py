from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

