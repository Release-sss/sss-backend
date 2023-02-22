FROM dongzoolee/sss-pipenv:latest

ENV PYTHONBUFFERED=1

RUN mkdir /srv/docker-django
ADD . /srv/docker-django

WORKDIR /srv/docker-django

RUN apk del build-deps

EXPOSE 8112

ENV DJANGO_SETTINGS_MODULE=sss.app.settings
CMD ["python", "manage.py", "runserver", "0.0.0.0:8112"]