from django.contrib.auth.models import User
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password',  'is_active',  'is_staff',  'is_superuser']
        # so it is only possible to write and not to read
        extra_kwargs = {
            'password': {'write_only': True}
        }