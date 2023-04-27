from rest_framework import serializers
from .models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id','content', 'created_date', 'is_completed']


class ToDoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['content',]