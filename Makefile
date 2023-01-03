migrate:
	python manage.py makemigrations --settings=marva_crm.settings.$(settings) &&
	python manage.py migrate --settings=marva_crm.settings.$(settings)
run:
	python manage.py runserver --settings=marva_crm.settings.$(settings)
static:
	python manage.py collectstatic --settings=marva_crm.settings.$(settings)
admin:
	python manage.py createsuperuser --settings=marva_crm.settings.$(settings)
