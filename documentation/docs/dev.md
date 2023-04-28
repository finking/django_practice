Вызов jupyter notebook:
`python manage.py shell_plus --notebook`


Для установки `jupyter_contrib_nbextensions` требуется:
#Установите команду nbextensions следующим образом:
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

#Установите nbextensions_configurator
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user

#Заметка: Если на странице нет элемента Hinterland или она неполная, командная строка выполняет:
jupyter contrib nbextension install --user --skip-running-check

# Ошибка при установке jupyter notebook
Требуется пакет pywinpty. Но он не устанавливается в некоторых версиях Python.
В файле dev_requirements.txt указана версия pywinpty==2.0.9, неофициальная версия 2.0.5.

Решения:
1. Переустановить Python другой версии.
2. Если переустановить Python не получается, то нужно   
2.1. вручную скачать pywinpty по ссылке https://github.com/spyder-ide/pywinpty и   
2.2. запустить через pip `pip install <путь до скаченного файла pywinpty>`
(решение: https://stackoverflow.com/questions/51260909/error-installing-jupyter-pywinpty-python)