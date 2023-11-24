migrate:
	python manage.py makemigrations && python manage.py migrate
run:
	python manage.py runserver
static:
	python manage.py collectstatic
admin:
	python manage.py createsuperuser
