from django import forms
from ..forms import ContactForm
import datetime
import pytest

# Переменные для проверки длины заполенных символов в поле
max_length_gt_100 = 'a' * 101
max_length_gt_500 = 'a' * 501

#Что тестируем и данные
# # TODO переделать на автоматические даты.
# @pytest.mark.parametrize(
#     'date_creation, subject, message, sender, cc_myself, validity',
#     [
#         # Рабочий вариант
#         ('2023-10-20', 'django lessons', 'I want to learn Django.', 'mail@mail.ru', 'cc_myself', True),
#
#         # Дата меньше текущей
#         ('2023-10-08', 'django lessons', 'Hi! I want to lern DjANGO', 'django@mail.ru', 'cc_myself', False),
#
#         # Дата старше текущей
#         ('2023-10-21', 'django lessons', 'Hi! I want to lern DjANGO', 'django@mail.ru', 'cc_myself', False),
#
#         # в емейл нет собаки
#         ('2022-02-09', 'django lessons', 'Hi! I want to lern DjANGO', 'djangomail.ru', 'cc_myself', False),
#     ]
# )
# def test_valid_contact_form(date_creation, subject, message, sender, cc_myself, validity):
#     form = ContactForm(data={
#         'date_creation': date_creation,
#         'subject': subject,
#         'message': message,
#         'sender': sender,
#         'cc_myself': cc_myself
#     })
#
#     # f = form.errors()
#     # print(f)
#
#     assert form.is_valid() is validity


@pytest.mark.parametrize(
    'date_creation, valid_date',
    [
        # Сегодняшняя дата
        (datetime.datetime.today(), True),
        # Дата младше текущей
        ('2023-10-26', False),
        # Дата позже текущей
        (datetime.datetime.today() + datetime.timedelta(days=1), False),
        # Проверка пустой строки
        ("", False)
    ]
)

@pytest.mark.parametrize(
    'subject, valid_subject',
    [
        # Обычный заголовок
        ('Header', True),
        # Заголовк превышающий лимит в 100 символов
        (max_length_gt_100, False),
        ('', False),
    ]
)

@pytest.mark.parametrize(
    'message, valid_message',
    [
        # Обычный текст
        ('This is some message', True),
        # Текст превышающий лимит в 500 символов
        (max_length_gt_500, False),
        ('', False),
    ]
)

@pytest.mark.parametrize(
    'sender, valid_sender',
    [
        # Валидный email
        ('tt@mail.ru', True),
        # Неверный email
        ('tt', False),
        # Обязательное поле
        ('', False),
    ]
)

@pytest.mark.parametrize(
    'cc_myself, valid_cc_myself',
    [
        ('cc_myself', True), # Не понятно, почему для чек-бокса указываем именно имя этого поля.
        # (),
        # (),
    ]
)


def test_contact_form(date_creation, subject, message, sender, cc_myself,
                      valid_date, valid_subject, valid_message, valid_sender, valid_cc_myself):
    form = ContactForm(data={
        "date_creation": date_creation,
        "subject": subject,
        "message": message,
        "sender": sender,
        "cc_myself": cc_myself
    })
    
    f = form.errors.as_data()
    print(f)
    
    assert form.is_valid() is (valid_date and valid_subject and valid_message and valid_sender and valid_cc_myself)
