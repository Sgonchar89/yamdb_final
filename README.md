![YaMDb workflow](https://github.com/Sgonchar89/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

API развернут по адресу http://84.252.142.247/api/v1/

# api_yamdb
REST API для сервиса YaMDb — базы отзывов о фильмах, книгах и музыке. (Коллективный проект 3 студентов Яндекс.Практикум)


## Описание

API для сервиса YaMDb.

Позволяет работать со следующими сущностями:

Отзывы 

Коментарии к отзывам

Пользователи 

Категории (типы) произведений

Категории жанров

Произведения (на которые пишут отзывы)

## Запуск проекта через docker

### Установка

#### Сборка и запуск контейнера
```bash
docker-compose up -d --build
```
#### База данных
```bash
docker-compose exec web python manage.py makemigrations --noinput
```
```bash
docker-compose exec web python manage.py migrate --noinput
```

### Использование

#### Создание суперпользователя Django
```bash
docker-compose exec web python manage.py createsuperuser
```
#### Сбор статических файлов
```bash
docker-compose exec web python manage.py collectstatic --no-input 
```
#### Импорт данных в .json
```bash
docker-compose run web python manage.py loaddata path/to/your/json
```
#### Выключение контейнера
```bash
docker-compose down
```
#### Удалить все неактивные (остановленные) контейнеры
```bash
docker container prune
```
#### Удалить в ненужные образы
```bash
docker image prune
```
#### Описание .env файла 
Этот файл содержит переменные окружения для работы с базой данных:

DB_ENGINE=django.db.backends.postgresql - тут указываем, с какой БД работает приложение 

DB_NAME=<имя_базы_данных> - тут указываем имя базы данных

POSTGRES_USER=<логин> - тут указываем логин для подключения к базе данных

POSTGRES_PASSWORD=<пароль> - пароль для подключения к БД 

DB_HOST=db - название сервиса (контейнера)

DB_PORT=5432 - порт для подключения к БД 

## Участники 
[Sgonchar89](https://github.com/Sgonchar89) - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.

[UlianaVo](https://github.com/UlianaVo) - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

[LasBazza](https://github.com/LasBazza) - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.