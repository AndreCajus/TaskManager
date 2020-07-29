from rest_framework import serializers
from .models import Task


class TaskSerializerFullAcess(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states']
        extra_kwargs = {
            'id': {'read_only': True}
        }


# so the states is always default on create operation and only admins can update it
class TaskSerializerBasicAccess(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states', 'author']
        extra_kwargs = {
            'states': {'read_only': True},
            'author': {'read_only': True},
            'id': {'read_only': True}
        }




