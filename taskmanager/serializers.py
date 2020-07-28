from rest_framework import serializers
from .models import Task


# so the states is always default on create operation and only admins can update it
class TaskSerializerBasicAccess(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states']
        extra_kwargs = {
            'states': {'read_only': True}
        }


class TaskSerializerFullAcess(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states', 'author']
