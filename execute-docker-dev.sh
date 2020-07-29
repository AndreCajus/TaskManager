#!bin/bash

python3.8 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('useradmin', 'admin@gmail.com', 'teste123?Aa')" | python3.8 manage.py shell

exec gunicorn --bind 0.0.0.0:8080 --workers 4 project.wsgi