DOCKER_COMPOSE_RUN = docker-compose run --rm
MANAGE_PY = ${DOCKER_COMPOSE_RUN} bookhub-backend python manage.py

run:
	${DOCKER_COMPOSE_RUN} --service-ports reverseproxy

create_migrations:
	${MANAGE_PY} makemigrations

migrate:
	${MANAGE_PY} migrate --no-input

clean_db:
	${MANAGE_PY} flush --no-input

load_fxtures:
	${MANAGE_PY} loaddata demo.yaml

create_fixtures:
	${MANAGE_PY} dumpdata \
		--natural-foreign \
		--exclude auth.permission \
		--exclude admin.logentry \
		--exclude sessions.session \
		--exclude contenttypes \
		--indent 2 \
		--output demo.yaml
