from rest_framework import serializers

from .models import Task

# so the states is always default on create operation and only admins can update it
class TaskSerializerForValidation(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'loc_geo', 'creation_date', 'update_date', 'category']


class TaskSerializerValidation(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'loc_geo', 'creation_date', 'update_date', 'category', 'states', 'author']


    #TRASFORMAR ISTO EM UM SO SERIALIZER E TRATAR DE MOSTRAR O AUTHOR USERNAME EM VEZ DO ID!!!!

