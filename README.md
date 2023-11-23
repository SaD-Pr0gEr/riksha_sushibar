# Django Basic Project config


## Installation

* Clone repository
```shell
git clone https://github.com/SaD-Pr0gEr/django_basic_project.git
```

* Install dependencies
```shell
#prod
pipenv install

#dev
pipenv install --dev
```

## Setup and run first time
This script sets dev settings, makes migrations and runs dev server
```shell
sh ./setup.sh
```

## Run
Run project with make
```shell
make run settings=dev
# prod settings
make run settings=prod
```
## !!!WARNING!!!
Don't use make run on production(use gunicorn/uvicorn etc.)

## NOTE
when you create your django apps in need directory, don't  forget register app in `INSTALLED_APPS` 
with absolute package path(aka `apps.your_app_path.apps.YourAppConfig`) and change `name` attribute 
on your app's `apps.py` to `apps.path_to_app`
