# Вопросы, возникающие при разработке.

### Mkdocs
1. Почему прописывали site_dir: 'wiki/GENERIC/generic/build' в файле mkdocs.yml
2. Не поменялся фавикон для wiki, хотя положил его в папку docs/img, как написано в документации
***
### Settings.
Не понятно, почему прописывали DIRS.        
              
         'DIRS': [os.path.join(BASE_DIR, 'templates'),],
У других авторов был просто пустой список 
`'DIRS': []:`

***
### Изучить модули
Модуль sys  
Модуль os  
pathlib (path)  
***

### ForeignKey and ManyToMany
- `related_name` в отношениях Django