.PHONY: docker-up
docker-up:
	docker-compose rm postgres api
	docker-compose up --build

.PHONY: django-up
flask-up:
	venv/bin/python manage.py runserver