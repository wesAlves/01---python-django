from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from todoBackend.models import TodoList

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields =  ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  TodoList
        fields =  '__all__'