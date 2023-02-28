# packages update/install
python3 -m pip install --upgrade pip
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt

# switch folder
cd steamauthentication

# ask for new super user creation
echo 'Do you want to create a new superuser? [y/n]'
read superuser
if [ $superuser = 'y']
then
   python3 manage.py createsuperuser
fi

# start
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
