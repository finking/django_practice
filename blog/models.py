from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.template.defaultfilters import slugify as django_slugify
from django.urls import reverse
from django.utils import timezone
# from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Словарь для преобразования киррилицы
alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


# функция для преобразования кириллицы в латиницу
def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Post(models.Model):

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    title = models.CharField(max_length=2000, db_index=True, help_text="не более 200 символов", verbose_name='Заголовок')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text="не более 5000 символов")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # в url при использовании slug обязательно добавлять id + get_absolute_url()
    slug = models.SlugField(max_length=50)
    likes_post = models.ManyToManyField(User, related_name='likes_post', blank=True, verbose_name='Лайки')
    saves_posts = models.ManyToManyField(User, related_name='saves_posts', blank=True, verbose_name='Сохраненные посты')

    # методы модели
    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title, allow_unicode=True)
    #     super(Post, self).save(*args, **kwargs)

    def total_likes_post(self):
        return self.likes_post.count()

    def total_saves_posts(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk, 'slug': self.slug})


@receiver(pre_save, sender=Post)
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    

# Модель комментариев блога
class Comment(models.Model):
    
    post = models.ForeignKey(Post, related_name='comments_blog', on_delete=models.CASCADE)
    name_author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    likes_commet = models.ManyToManyField(User, related_name='likes_blog_comment', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='replies_comment', on_delete=models.CASCADE)

    def total_likes_comment(self):
        return self.likes_commet.count()
    
    def __str__(self):
        return f"{self.post.title} - {self.name_author} - {self.id}"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk, 'slug': self.post.slug})
