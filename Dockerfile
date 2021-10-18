#FROM python:3.8.5
#
#RUN mkdir /code
#WORKDIR /code
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY . .
#CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

FROM python:3.8
COPY ./ /app
RUN pip install -r /app/requirements.txt
WORKDIR /app/infra_project/
CMD python manage.py runserver 0:5000