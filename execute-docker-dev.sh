#!bin/bash

python3.8 manage.py migrate
echo "yes" | python3.8 manage.py collectstatic #validar sem isto
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('useradmin', 'admin@gmail.com', 'teste123?Aa')" | python3.8 manage.py shell
DJANGO_SUPERUSER_PASSWORD="teste123?Aa"
python3.8 manage.py createsuperuser --no-input --username="useradmin" --email="my_user@domain.com"
exec gunicorn --bind 0.0.0.0:8080 --workers 4 project.wsgi