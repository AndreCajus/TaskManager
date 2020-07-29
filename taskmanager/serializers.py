from rest_framework import serializers
from .models import Task
from django_filters import rest_framework as filters


class TaskSerializerFullAcess(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states']
        extra_kwargs = {
            'id': {'read_only': True},
            'creation_date': {'read_only': True},
            'update_date': {'read_only': True},
        }


# so the states is always default on create operation and only admins can update it
class TaskSerializerBasicAccess(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states', 'author']
        extra_kwargs = {
            'states': {'read_only': True},
            'author': {'read_only': True},
            'id': {'read_only': True},
            'creation_date': {'read_only': True},
            'update_date': {'read_only': True},
        }

# so the states is always default on create operation and only admins can update it
class TaskSerializerValidation(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['states']


from django.db.models import Q
from django.contrib.gis.geos import Point
# to be used by taskFilter at the view
class TaskFilter(filters.FilterSet):

    class Meta:
        model = Task
        fields = ('author', 'category')




