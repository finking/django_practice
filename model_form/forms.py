from django.forms import ModelForm, Textarea
from .models import Author, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "title", "birth_date"]
        widgets = {
            'name': Textarea(attrs={'cols': '10', 'rows': '5'}),  # TODO Разобраться почему cols "не работает"
        }
        labels = {
            'name': 'Description'
        }
        help_texts = {
            'name': "Описание должно быть не более 100 символов."
        }
        error_messages = {
            'name': {
                'max_length': "Вы написали больше символов, чем разрешено."
            },
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "authors"]
