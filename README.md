![YaMDb workflow](https://github.com/Sgonchar89/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


# api_yamdb
REST API for YaMDb service - movie, book and music reviews database. (Collective project of 3 Yandex.Practicum students)

## Description

API for YaMDb service.

Allows you to work with the following entities:

Reviews

Comments on reviews

Users  

Categories (types) of works

Genre categories

Works (for which users write reviews)

## Running the project via docker

### Installation

#### Container assembly and startup
```bash
docker-compose up -d --build
```
#### Database
```bash
docker-compose exec web python manage.py makemigrations --noinput
```
```bash
docker-compose exec web python manage.py migrate --noinput
```

### Exploitation

#### Creating a Django superuser
```bash
docker-compose exec web python manage.py createsuperuser
```
#### Collecting static files
```bash
docker-compose exec web python manage.py collectstatic --no-input 
```
#### Importing data into .json
```bash
docker-compose run web python manage.py loaddata path/to/your/json
```
#### Turning off the container
```bash
docker-compose down
```
#### Deleting all inactive (stopped) containers
```bash
docker container prune
```
#### Removing all unwanted images
```bash
docker image prune
```
#### Description of the .env file 
This file contains environment variables for working with the database:

DB_ENGINE=django.db.backends.postgresql - Here we specify which database the application works with  

DB_NAME=<database_name> - Here we specify the name of the database

POSTGRES_USER=<postgres_login> - Here you specify the login to connect to the database

POSTGRES_PASSWORD=<postgres_password> - Password to connect to the database 

DB_HOST=db - Service name (container)

DB_PORT=5432 - DB connection port 

## Participants  
[Sgonchar89](https://github.com/Sgonchar89) - Review and Comments: models and views, endpoints, access rights for requests. Ratings of works.

[UlianaVo](https://github.com/UlianaVo) - Categories, Genres, and Titles: models, views, and endpoints for them.

[LasBazza](https://github.com/LasBazza) - User management (Auth and Users): registration and authentication system, access rights, work with token, e-mail confirmation system, fields.
