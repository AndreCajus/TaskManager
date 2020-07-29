#!bin/bash

python3.8 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python3.8 manage.py shell

exec gunicorn --bind 0.0.0.0:8000 --workers 4 project.wsgi