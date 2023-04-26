from django.db import models


class Sites(models.Model):
    """
    Добавление сайтов, которые интересны
    """
    class Meta:
        ordering = ('-name',)  # Todo проверить без скобок.
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'

    name = models.CharField(max_length=80,
                            verbose_name='Название сайта',
                            help_text='Не более 80 символов')

    website = models.URLField(verbose_name='Адрес сайта', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Nick(models.Model):
    """
    Ник или имя пользователя, владельца контента
    """
    class Meta:
        verbose_name = 'Имя или ник автора'
        verbose_name_plural = 'Имена или ники авторов'

    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    personal_website = models.URLField(blank=True, null=True)
    picture = models.ImageField(upload_to='info_notes_pictures', null=True, default='nick.png')

    def __str__(self):
        return self.name


class Notes(models.Model):
    """
    Для хранения заметок, которые нам понравились.
    """
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    title = models.CharField(max_length=120)
    nick = models.ManyToManyField('Nick')
    sites = models.ForeignKey(Sites, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
