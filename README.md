## Serving Project Locally

### Django SECRET KEY Generator: https://djecrety.ir/ (generate one and paste in settings.py file)

## install python 3: 
https://www.python.org/downloads/

### cloning the repository
git clone https://github.com/mhope-2/django_blog.git

## create a virtual environment
python3 -m venv env_name

## activate virtual environment
source env_name/bin/activate 

## Install required packages
pip install -r requirements.txt

## Make migrations
run: python manage.py makemigrations
run: python manage.py migrate

## Run app
python manage.py runserver<br>
app will be served on http://127.0.0.1:8000<br>


