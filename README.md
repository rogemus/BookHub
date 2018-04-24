# BookHub
Projekt grupowy na Systemy Informatyczne

## Build Status
[![Build Status](https://travis-ci.org/rogemus/BookHub.svg?branch=master)](https://travis-ci.org/rogemus/BookHub)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4ff4087c832b45d4a46eb3bd8157fc6e)](https://www.codacy.com/app/bookhub-corporation/BookHub?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rogemus/BookHub&amp;utm_campaign=Badge_Grade)

## Run BookHub
1. Add to your `/etc/hosts` record for `bookhub.com` to point to `127.0.0.1`.

	```bash
	127.0.0.1   localhost bookhub.com
	```
2. Start BookHub services with command

	```bash
	make run-prod
	```
3. If you want load some example data

	```bash
	make load_fxtures
	```

## Developing (with Docker)

### I want develop BookHub Backend

Run Docker containers with DEV profile and syncing /app directory. Django server should detect your local changes and automaticly reload.

```bash
make run-dev
```

###  I want develop BookHub Frontend

1. Start backend service

	```bash
	make run-backend
	```
	
1. Start frontend server, see details [here](/BookHub-frontend/)



