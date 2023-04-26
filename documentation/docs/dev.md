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