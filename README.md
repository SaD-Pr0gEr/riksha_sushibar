# Riksha sushibar
Simple shop to buy sushi


## Installation

* Clone repository
```shell
# ssh
git clone git@github.com:SaD-Pr0gEr/riksha_sushibar.git

#https
git clone https://github.com/SaD-Pr0gEr/riksha_sushibar.git
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

# with prod settings manually
python manage.py runserver --settings=core.settings.prod
# or with gunicorn
gunicorn core.wsgi:application --bind 127.0.0.1:8000
```
## !!!WARNING!!!
Don't use make run on production(use gunicorn/uvicorn etc.)

## NOTE
when you create your django apps in need directory, don't  forget register app in `INSTALLED_APPS` 
with absolute package path(aka `apps.your_app_path.apps.YourAppConfig`) and change `name` attribute 
on your app's `apps.py` to `apps.path_to_app`
