# Backend




To run after cloning


Create Virtual Envirolment:

python -m venv venv

To activate virtual Envirolment:

For windows:
./venv/Script/activate

For Linux or mac:
source venv/bin/activate

Installing dependency:

pip install -r req.txt



To use application 
cd backend 
To parse and save log to centralized log db: python manage.py logparse

To start server: python manage.py runserver

In default server will start in localhost:8000



To make db:
#settings.py


DATABASES = {
    'default': {
        'ENGINE': 'DB-Engine',
        'NAME': 'DB-name',
        'USER': 'DB-User',
        'PASSWORD': 'DB-password',
        'HOST': 'Host name', 
        'PORT': 'port',
    }
}