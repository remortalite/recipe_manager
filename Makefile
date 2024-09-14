all: install

install:
	poetry install --without=dev

install-dev:
	poetry install --with dev

run: install
	poetry run python manage.py runserver