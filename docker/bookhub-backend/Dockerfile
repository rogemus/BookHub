FROM python:3.6-slim

ENV DJANGO_SETTINGS_MODULE=BookHub.settings.prod

RUN mkdir /app /var/log/bookhub
WORKDIR /app
ADD ./requirements/prod.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

RUN ln -sf /dev/stdout /var/log/bookhub/access.log \
	&& ln -sf /dev/stderr /var/log/bookhub/error.log

EXPOSE 8000

CMD ["gunicorn", "--name", "app_server", "--workers", "2", "--bind", "0.0.0.0:8000", "BookHub.wsgi:application", \
    "--access-logfile", "/var/log/bookhub/access.log", "--error-logfile", "/var/log/bookhub/error.log"]
