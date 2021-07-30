.PHONY: docker-up
docker-up:
	docker-compose rm db api
	docker-compose up --build

.PHONY: django-up
django-up:
	venv/bin/python manage.py runserver

.PHONY: db-seed
db-seed:
	venv/bin/python manage.py seed post --number=100
