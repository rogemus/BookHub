FROM python:3.6-slim

COPY . /code/

WORKDIR /code/

RUN pip install -r requirements/dev.txt

ENV DJANGO_SETTINGS_MODULE BookHub.settings.local

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
