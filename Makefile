DOCKER_COMPOSE_EXEC = docker-compose exec
MANAGE_PY = ${DOCKER_COMPOSE_EXEC} backend python manage.py

run:
	docker-compose -f docker-compose.yml -f docker-compose.${ENV}.yml up -d

run-solo:
	docker-compose -f docker-compose.yml -f docker-compose.${ENV}.yml up --no-deps -d ${SERVICE}

run-dev: ENV=dev
run-dev: run migrate load_fxtures

run-prod: ENV=prod
run-prod: run migrate

run-build:
	docker-compose -f docker-compose.yml -f docker-compose.build.yml build --no-cache

run-backend: ENV=dev
run-backend: SERVICE=backend
run-backend: run-solo migrate load_fxtures

create_migrations:
	${MANAGE_PY} makemigrations

migrate:
	${MANAGE_PY} migrate --no-input

clean_db:
	${MANAGE_PY} flush --no-input

load_fxtures:
	docker cp demo.json backend:/app/demo.json
	${MANAGE_PY} loaddata demo.json

create_fixtures:
	${MANAGE_PY} dumpdata \
		--natural-foreign \
		--exclude auth.permission \
		--exclude admin.logentry \
		--exclude sessions.session \
		--exclude contenttypes \
		--indent 4 > demo.json

