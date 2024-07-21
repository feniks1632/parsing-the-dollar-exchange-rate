# parsing-the-dollar-exchange-rate
актуальный курс доллара и 10 последних записей

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)


### Функциональность

- Получение текущих данных о курсе доллара.
- Отображение 10 последних запросов.
- Обработка ошибок для некорректных вводов и проблем с API.


# Порядок запуска

## 1  Склонировать репозиторий 
```bash
   git clone <название репозитория>
   cd <ваш_репозиторий>
```
## 2. Получить ключ на сайте
https://www.exchangerate-api.com/

## 3. Ввести его в .env в параметр "API_KEY"

## 4. Создайте и активируйте виртуальное окружение:
```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Window
```

## 5. Установите зависимости проекта
```bash
   pip install -r requirements.txt
```
## 6. Выполните миграции базы данных
```bash
   python manage.py makemigrations
   python manage.py migrate
```

## 7. Запустить сервер разработки
```bash
   python manage.py runserver
```

## 8. Перейти на са сайт 
## http://127.0.0.1:8000/get_current_usd/



#### Используемые технологии
- Python 3.12
- Django 3.5
- API сервиса валют 


#### Автор проекта

Никита Бражников - (https://github.com/feniks1632)
