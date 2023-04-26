from django.db import models

from django.db import models
from django.urls import reverse


class Page(models.Model):
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    name = models.CharField(max_length=160,
                            verbose_name='Название',
                            help_text='Максимум 160 символов')
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('yes_ns:detail_url', kwargs={'id': self.id})

    def __str__(self):
        return self.name