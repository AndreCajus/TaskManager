from rest_framework import serializers
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password',  'is_active',  'is_staff',  'is_superuser']
        # so people cant read what is on password arg when the request is made (hides password field)
        extra_kwargs = {
            'password': {'write_only': True}
        }