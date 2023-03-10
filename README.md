# Steam signin system with Django

## How to run

### 1. Environment variables

You'll need to change name to the "template.env" file from "template.env" to ".env" and fill all the empty fields.
You'll have to deal also with the ABSOLUTE_URL field:
Depending on the configuration it has to be 0.0.0.0 (within docker) or localhost (without docker)

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

If you want to connect to connect to your postgres database youhave to run django without docker

### Environment variables and SSL

It's not necessary to have a certifcate if you don't run the website in docker but it's not bad the have a bit more security on the internet. (follow the above 1. and 2. steps)

### 2. PostgreSQL

First, let's start a postgres db in docker (because it is simpler to setup).

Just run:
`docker run --name some-postgres -p 5432:5432 -e POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres -d postgres`
You can change port user and password if you wish, but remember to change them also in the env file

### 3. Django set up

You needto change the database used by Django. Go to "django-steam-signin/webapp/webapp" and open the file settings.py.
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