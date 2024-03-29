from django.db import models
from django.urls import reverse

TITLE_CHOICE = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
    

class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    authors = models.ManyToManyField(Author)
    
    def get_authors(self):
        return ", ".join([p.name for p in self.authors.all()])
