from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from todoBackend.models import TodoList
from todoListRestAPI.serializers.serializers import UserSerializer, GroupSerializer, TodoSerializer



# class UserViewSet(viewsets.ModelViewSet):
#     #API endpoint that allows users to be viewed or edited.

#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     perissions_class = [permissions.IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     #API endipoint that allows groups to be viewed or edited.

#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     perissions_class = [permissions.IsAuthenticated]

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
    

