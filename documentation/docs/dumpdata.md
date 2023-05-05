# Информация по экспорту/импорту базы данных в json

## **Команды**:
- `python manage.py loaddata db.json` - загрузка бд с именем db
- `python manage.py dumpdata name_app.name_model --indent 2  > model_name_db.json` - выгрузка определенной модели `model_name` 
из приложения `name_app` в файл с именем `model_name_db` в формате json  
(для выгрузки в <ins>определенную</ins> папку: `name_app/fixstures/model_name_db.json`)  
- `python manage.py dumpdata --indent 2  > full_app.json` - выгрузка всего проекта  
- `python manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json` - перенесение бд с локального компа
на боевой, исключая `auth.permission` и `exclude contenttypes`

## Официальная документация
Ссылка: https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata  
Код: `django-admin dumpdata [app_label[.ModelName] [app_label[.ModelName] ...]]`  
Outputs to standard output all data in the database associated with the named application(s).  
If no application name is provided, all installed applications will be dumped.  
The output of dumpdata can be used as input for loaddata.  

Ссылка: https://docs.djangoproject.com/en/4.1/ref/django-admin/#loaddata  
Код: `django-admin loaddata fixture [fixture ...]`
Searches for and loads the contents of the named fixture into the database.

***
# Проблемы
- кодировки


Если при dump'e получается аббракадабра (открывается как UTF-8, но
отображается как Windows-1251), то необходимо добавить перед `manage.py` 
дополнительную команду `-Xutf8`, т.е.
`python -Xutf8 manage.py dumpdata name_app.name_model --indent 2  > model_name_db.json`


- Ошибки в ContentType  
Команда `python manage.py loaddata db.json` вызывает ошибку: `django.db.utils.IntegrityError: Problem installing fixture 'C:\PycharmProjects\django_practice\django_practice\practice_django.json': Could not load contenttypes.ContentType(pk=10): UNIQUE constraint failed: django_content_type.app_lab
el, django_content_type.model.`

Чтобы избежать эту ошибку, из дампа лучше исключить некоторые таблицы: `python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > dump.json
`

Если избежать не получается, то нужно поменять `pk` на `id` в "проблемных" таблицах. Или вообще эти таблицы удалить.

Ссылка на решение проблемы: https://stackoverflow.com/questions/40193992/django-loaddata-unique-constraint-failed
***
