from django import forms
from ..forms import ContactForm
import datetime
import pytest


#Что тестируем и данные
# TODO переделать на автоматические даты.
@pytest.mark.parametrize(
    'date_creation, subject, message, sender, cc_myself, validity',
    [
        # Рабочий вариант
        ('2023-10-20', 'django lessons', 'I want to learn Django.', 'mail@mail.ru', 'cc_myself', True),
        
        # Дата меньше текущей
        ('2023-10-08', 'django lessons', 'Hi! I want to lern DjANGO', 'django@mail.ru', 'cc_myself', False),
    
        # Дата старше текущей
        ('2023-10-21', 'django lessons', 'Hi! I want to lern DjANGO', 'django@mail.ru', 'cc_myself', False),
    
        # в емейл нет собаки
        ('2022-02-09', 'django lessons', 'Hi! I want to lern DjANGO', 'djangomail.ru', 'cc_myself', False),
    ]
)
def test_valid_contact_form(date_creation, subject, message, sender, cc_myself, validity):
    form = ContactForm(data={
        'date_creation': date_creation,
        'subject': subject,
        'message': message,
        'sender': sender,
        'cc_myself': cc_myself
    })
    
    # f = form.errors()
    # print(f)
    
    assert form.is_valid() is validity
