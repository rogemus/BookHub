DOCKER_COMPOSE_RUN = docker-compose run --rm
DOCKER_COMPOSE_EXEC = docker-compose exec
MANAGE_PY = ${DOCKER_COMPOSE_EXEC} bookhub-backend python manage.py

run:
	${DOCKER_COMPOSE_RUN} --service-ports reverseproxy

create_migrations:
	${MANAGE_PY} makemigrations

migrate:
	${MANAGE_PY} migrate --no-input

clean_db:
	${MANAGE_PY} flush --no-input

load_fxtures:
	docker cp demo.json bookhub-backend:/app/demo.json
	${MANAGE_PY} loaddata demo.json

create_fixtures:
	${MANAGE_PY} dumpdata \
		--natural-foreign \
		--exclude auth.permission \
		--exclude admin.logentry \
		--exclude sessions.session \
		--exclude contenttypes \
		--indent 4 > demo.json

maciej:
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
