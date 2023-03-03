# CLI commands:
# - docker build . -t django-webapp-sqlite
# - docker run --name django-sqlite --env-file .env -p 8000:8000 -d django-webapp-sqlite

# base image
FROM python

# setup working directory
ENV DockerHOME=/home/app/webapp
# create work directory
RUN mkdir -p $DockerHOME
# # set work directory (where your code lives)
WORKDIR $DockerHOME
# copy the whole project to your docker home directory
COPY . $DockerHOME

# set environment variables
# Python avoids to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Python doesn't buffer stdin/stdout
ENV PYTHONUNBUFFERED 1

# update pip
RUN pip install --upgrade pip
# install all dependencies
RUN pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# run start file
#RUN ["chmod", "+x", "./startup.sh"]
#ENTRYPOINT [ "./startup.sh" ]

# make migrations
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate

# run the server
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python3 manage.py makemigrations; python3 manage.py migrate; python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0.0.0.0:${APP_PORT}
