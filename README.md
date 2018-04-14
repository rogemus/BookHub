# BookHub
Projekt grupowy na Systemy Informatyczne

## Build Status
[![Build Status](https://travis-ci.org/rogemus/BookHub.svg?branch=master)](https://travis-ci.org/rogemus/BookHub)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ff4087c832b45d4a46eb3bd8157fc6e)](https://www.codacy.com/app/bookhub-corporation/BookHub?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rogemus/BookHub&amp;utm_campaign=Badge_Grade)

## Developing
1. Create VirtualEnv ```python3.6 -m venv venv```
2. Activate VirtualEnv ```source venv/bin/activate```
3. Install req ```pip install -r BookHub/requirements/dev.txt```
4. Navigate to ```BookHub``` directory ```cd BookHub```
5. Export settings ```export DJANGO_SETTINGS_MODULE='BookHub.settings.local'```
6. Make DB migrations ```python manage.py migrate```
7. Create Admin user ```python manage.py createsuperuser --email admin@example.com --username admin```
8. Load demo content ```./manage.py loaddata db.json```
9. Start server ```python manage.py runserver 127.0.0.1:8080```

Resource | URL
--- | ---
API|http://127.0.0.1:8080/api/
Admin|http://127.0.0.1:8080/admin/


