DOCKER_COMPOSE_RUN = docker-compose run --rm
MANAGE_PY = ${DOCKER_COMPOSE_RUN} web python manage.py

run:
	${DOCKER_COMPOSE_RUN} --service-ports web

create_migrations:
	${MANAGE_PY} makemigrations

migrate:
	${MANAGE_PY} migrate --no-input

clean_db:
	${MANAGE_PY} flush --no-input

load_fxtures:
	${MANAGE_PY} loaddata demo.json

create_fixtures:
	${MANAGE_PY} dumpdata \
		--natural-foreign \
		--exclude auth.permission \
		--exclude admin.logentry \
		--exclude sessions.session \
		--exclude contenttypes \
		--indent 4 > demo.json
