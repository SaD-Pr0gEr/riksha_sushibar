migrate:
	python manage.py makemigrations --settings=config.settings.$(settings) && python manage.py migrate --settings=config.settings.$(settings)
run:
	python manage.py runserver --settings=config.settings.$(settings)
static:
	python manage.py collectstatic --settings=config.settings.$(settings)
admin:
	python manage.py createsuperuser --settings=config.settings.$(settings)
