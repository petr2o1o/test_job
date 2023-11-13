FROM python:latest
RUN apt-get update \
 && apt-get install -y python3-django postgresql-client
WORKDIR /usr/src/app
RUN pip install Django psycopg2 && pip install Django==4.2.7
COPY ../* .
EXPOSE 8000
ENTRYPOINT sleep 10 && python3 manage.py runserver 0.0.0.0:8000
