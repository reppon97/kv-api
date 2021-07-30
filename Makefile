.PHONY: docker-up
docker-up:
	docker-compose rm db api
	docker-compose up --build

.PHONY: django-up
flask-up:
	venv/bin/python manage.py runserver