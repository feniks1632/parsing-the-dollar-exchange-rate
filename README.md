# parsing-the-dollar-exchange-rate
актуальный курс доллара и 10 последних записей
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)


### Функциональность

- Получение текущих данных о курсе доллара.
- Отображение 10 последних запросов.
- Обработка ошибок для некорректных вводов и проблем с API.


# Порядок запуска
# 1. Получить ключ на сайте
https://www.exchangerate-api.com/
# 2. Ввести его в .env в параметр "API_KEY"
# 3. Установить зависимости проекта
pip install -r requirements.txt
# Произвести миграции
5. python manage.py migrate
# Запустить сервер разработки
7. 1. python manage.py runserver
   2. Перейти на адрес http://127.0.0.1:8000/get_current_usd/


#### Используемые технологии
- Python 3.12
- Django 3.5
- API сервиса валют 


#### Автор проекта

Никита Бражников - (https://github.com/feniks1632)