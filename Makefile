.PHONY: docker-up
docker-up:
	docker-compose up --build

.PHONY: django-up
django-up:
	venv/bin/python manage.py runserver

.PHONY: db-seed
db-seed:
	venv/bin/python manage.py seed post --number=100

.PHONY: docker-init
docker-init:
	docker-compose run api python manage.py makemigrations
	docker-compose run api python manage.py migrate
	docker-compose run api python manage.py createsuperuser --noinput
	docker-compose run api python manage.py seed post --number=100
