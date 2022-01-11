1 step: clone this repository

    git clone 

2 step: set enviroment

    python3 -m venv venv

    source ./venv/bin/activate

3 step: install all pakages

    pip install -r requirements.txt

4 step: migrate models to database

    python manage.py makemigrations
    
    python manage.py migrate

5 step: start project

    python manage.py runserver


API doc. uri: /swagger/
