from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify as django_slugify
# from django.utils.text import slugify


# Словарь для преобразования киррилицы
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


# функция для преобразования кириллицы в латиницу
def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Discussion(models.Model):

    class Meta:
        verbose_name = 'Дискуссия'
        verbose_name_plural = 'Дискуссии'

    title = models.CharField(max_length=200,
                             help_text='не более 200 символов', db_index=True)
    content = RichTextField(blank=True, null=True,
                            help_text="не более 5000 символов", max_length=5000)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)  # unique=True подумать
    likes_discussion = models.ManyToManyField(
        User, related_name='discussion_likes', blank=True, verbose_name='Лайки')
    saves_discussion = models.ManyToManyField(
        User, related_name="blog_discussion_save", blank=True, verbose_name='Сохранённые обсуждения пользователя')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Discussion, self).save(*args, **kwargs)

    def total_likes_discussion(self):
        return self.likes_discussion.count()

    def total_saves_discussions(self):
        return self.saves_discussion.count()

    def get_absolute_url(self):
        return reverse('discussion-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # методы модели
    def __str__(self):
        return self.title


@receiver(pre_save, sender=Discussion)
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)