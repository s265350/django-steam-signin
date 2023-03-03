# django-steam-signin

## How to run

### 1. Create a SSL certificate first

This instance works only if with an SSL certifcate
You can create one following this tutorial: https://timonweb.com/django/https-django-development-server-ssl-certificate/
Put both cert and key files inside the "django-steam-signin/webapp" folder.

### 2. It' better to run in a Docker container

Download the CLI tool or the Docker application from their website: https://www.docker.com

### 3. Create the docker image

In the terminal navigate to the "django-steam-signin/webapp" folder and  run this command:
`docker build . -t django-ssl-sqlite`
It may take sometime.

### 3. Run the docker container

Run this command in the same terminal:
`docker run --name django-sqlite --env-file .env -p 8000:8000 django-ssl-sqlite`
It will take some time to be ready after it starts running.
Run it in detach mode if you have the docker application:
`docker run --name django-sqlite --env-file .env -p 8000:8000 -d django-ssl-sqlite`

### 4. Browser

Open your browser and go to: https://0.0.0.0/8000