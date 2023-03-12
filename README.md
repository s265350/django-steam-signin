# Steam signin system with Django

## How to run

### 1. Environment variables

You'll need to change name to the "template.env" file to ".env" and fill all the empty fields:
- SECRET_KEY: your Django project secret key
- STEAM_API_KEY: your Steam secret key
- ABSOLUTE_URL: 0.0.0.0 (with docker) or 127.0.0.1 (without docker)

### 2. Create a SSL certificate

This instance works only if with an SSL certifcate
You can create one following this tutorial: https://timonweb.com/django/https-django-development-server-ssl-certificate/
Put both cert and key files inside the "django-steam-signin/webapp" folder.

### 3. It's better to run in a Docker container

Download the CLI tool or the Docker application from their website: https://www.docker.com

### 4. Create the docker image

In the terminal navigate to the "django-steam-signin/webapp" folder and  run this command:
`docker build . -t django-ssl-sqlite`
It may take sometime.

### 5. Run the docker container

Run this command in the same terminal:
`docker run --name django-sqlite --env-file .env -p 8000:8000 django-ssl-sqlite`
It will take some time to be ready after it starts running.
Run it in detach mode if you have the docker application:
`docker run --name django-sqlite --env-file .env -p 8000:8000 -d django-ssl-sqlite`

### 6. Browser

Open your browser and go to: https://0.0.0.0/8000

## Run without docker

If you want to connect to connect to your postgres database you have to run django WITHOUT docker (for now).
Be sure to have python 3 installed.

### Environment variables and SSL

It's not necessary to have a certifcate if you don't run the website in docker but it's not bad the have a bit more security on the internet. (follow the above 1. and 2. steps)

### 3. PostgreSQL

First, let's start a postgres db in docker (because it is simpler to setup).

Just run:
`docker run --name some-postgres -p 5432:5432 -e POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres -d postgres`
You can change port user and password if you wish, but remember to change them also in the env file

### 4. Django set up

You need to change the database used by Django. Go to "django-steam-signin/webapp/webapp" and open the file settings.py.
It is set yet you only have to go tothe DATABASES section and swap the content ofthe 'default' and 'replica' databases.

from: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
   },
}

to:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
   },
    'replica': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   },
}

### 5. Environment

It is safer to install the dependencies inside a virtual environment, if you don't care just run the last command.
In the terminal navigate to the "django-steam-signin" folder and  run this commands:

`pip install --upgrade pip`

`pip install virtualenv`

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

### 6. Run the server

In the terminal navigate to the "django-steam-signin/webapp" folder and run this commands:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver_plus --cert-file cert.pem --key-file key.pem 127.0.0.1:$8000`

If you changed the ABSOLUTE_URL AND APP_PORT in the .env file change the last part of the last command accordingly

### 6. Exit the environment

Stop the server first with CTRL-C then run:

`deactivate`