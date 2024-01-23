# Klosers API

### Technologies
- Python 3.11.5
- Django 4.2
- Django Rest Framework 3.14
- Postgres 14
- Mailgun


## Get Started


```bash
$ python3 -m venv env
$ source env/bin/activate
$ git clone {URL}
$ cd klosers-api
$ touch .env

# enter shell to generate your SECRET_KEY
$ python3 manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
# copy the output and paste it in the .env file for SECRET_KEY
>>> exit()

# install the libraries from requirements.txt
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py runserver
```

### Add a New Library

```bash
$ pip3 install {library}
$ pip3 freeze > requirements.txt # to update requirements.txt
```


## Postgres Commands
No need to enter postgres shell to drop and create. Use the following commands instead.

```bash
$ createdb --username=postgres new_kloser_db
$ dropdb new_kloser_db
```

If you need to enter the Postgres shell 
```bash
$ psql new_kloser_db
>>> ...
>>> exit()
```


