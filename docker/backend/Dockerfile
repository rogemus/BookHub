FROM python:3.6.5-alpine3.6

LABEL version "1.0"
LABEL maintainer "BookHub Corporation <technical@bookhub.com>"


ENV STATIC_ROOT "/static"
ENV DJANGO_SETTINGS_MODULE "BookHub.settings.prod"
ENV DJANGO_SECRET_KEY "2k9ddxwa0wpk-cw7ay2%q-tf!el!%@t=hao6(__(dzg&yj!izo"

RUN mkdir ${STATIC_ROOT}

WORKDIR /app

COPY ./requirements/*.txt /app/requirements/

RUN pip install --no-cache-dir -r ./requirements/prod.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--name=app_server", "--workers=2", "--bind=0.0.0.0:8000", "BookHub.wsgi:application"]
