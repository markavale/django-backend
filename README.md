# django-backend-boilerplate

## Project Details
This Template includes dj-rest-auth for authentication, Token authentication and VueJS library installed in static folder.

## Project setup for virtualenv users
```
python3 -m venv venv
source venv/bin/activate (linux/Mac) || cd venv/scripts/ => activate (windows)
pip install -r requirements.txt
python manage.py makemigrations users
python manage.py migrate
python manage.py runserver
```

## Project setup for pipenv users
```
pipenv install
pipenv shell
python manage.py makemigrations users
python manage.py migrate
python manage.py runserver
```

## Create .env file for your env variables
Copy paste this and replace it with your own variables
```
[settings]
SECRET_KEY = 'your_awesome_secret_key!'
DJANGO_SETTINGS_MODULE = 'base.settings.dev'

[mysql-database-config | if you're using mysql] 
NAME=your_db_name
USER=your_db_user
PASSWORD=your_db_password
PORT=your_db_port
HOST=your_db_host

[email]
EMAIL_HOST_PASSWORD = 'your_email_pass'
EMAIL_HOST_USER = 'your_email'
```
See [Configuration Reference of python decouple](https://pypi.org/project/python-decouple/).



