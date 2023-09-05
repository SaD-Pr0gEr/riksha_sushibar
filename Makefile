migrate:
	python manage.py makemigrations --settings=core.settings.$(settings) && python manage.py migrate --settings=core.settings.$(settings)
run:
	python manage.py runserver --settings=core.settings.$(settings)
static:
	python manage.py collectstatic --settings=core.settings.$(settings)
admin:
	python manage.py createsuperuser --settings=core.settings.$(settings)
