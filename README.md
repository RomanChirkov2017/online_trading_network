# Онлайн-платформа торговой сети электроники

## Задание

* Создайте веб-приложение с API-интерфейсом и админ-панелью. 
* Создайте базу данных, используя миграции Django.

## Технические требования:
* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

## Требования к реализации:

### 1. Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из трех уровней:

* завод;
* розничная сеть;
* индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). 
Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, 
т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.

### 2. Каждое звено сети должно обладать следующими элементами:
* Название.

* Контакты:
- email,
- страна,
- город,
- улица,
- номер дома.
* Продукты:
- название,
- модель,
- дата выхода продукта на рынок.

* Поставщик (предыдущий по иерархии объект сети).

* Задолженность перед поставщиком в денежном выражении с точностью до копеек.
* Время создания (заполняется автоматически при создании).

### 3. Сделать вывод в админ-панели созданных объектов.
На странице объекта сети добавить:
- ссылку на «Поставщика»;
- фильтр по названию города;
- admin action, очищающий задолженность перед поставщиком у выбранных объектов.

### 4. Используя DRF, создать набор представлений:
- CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).
- Добавить возможность фильтрации объектов по определенной стране.

### 5. Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

----------------------------------------------------------------

## Используемый стэк:
* Python 3.11
* Django 4.2
* DRF 3.15.2
* PostgreSQL 14

## Документация проекта:

               "http://127.0.0.1:8000/swagger/"
               "http://127.0.0.1:8000/redoc/"

## Для запуска приложения:
* скопируйте данный репозиторий на локальный компьютер;

* создайте и заполните файл .env по шаблону из файла .env.sample;

* создайте БД, выполнив следующие команды в терминале:
- psql -U <DB_USER>;
- CREATE DATABASE <db_name>;
- \q.

* установите необходимые зависимости с помощью команды  pip install -r requirements.txt

* примените миграции, выполнив команду  python manage.py migrate

* запустите приложение, выполнив в терминале команду  python manage.py runserver.
