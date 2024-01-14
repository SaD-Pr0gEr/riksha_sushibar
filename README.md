# Django Project template


## Installation

* Clone repository
```shell
git clone https://github.com/SaD-Pr0gEr/django_basic_project.git
```

* Install dependencies & activate environment
```shell
#prod
pipenv install

#dev
pipenv install --dev

pipenv shell
```

## Install environment vars
* rename `example.env` to `.env` and set all values to actual values

## Run
Run project with make
```shell
make run

# RUN IT MANUALLY WITH SETTINGS
# dev
python manage.py runserver --settings=core.settings.dev
# prod settings
python manage.py runserver --settings=core.settings.prod
```
## !!!WARNING!!!
Don't use make run on production(use gunicorn/uvicorn etc.)

## NOTE
when you create your django apps in need directory, don't  forget register app in `INSTALLED_APPS` 
with absolute package path(aka `apps.your_app_path.apps.YourAppConfig`) and change `name` attribute 
on your app's `apps.py` to `apps.path_to_app`
