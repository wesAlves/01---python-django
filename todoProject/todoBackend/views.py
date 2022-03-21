from django.http import HttpResponse
from django.shortcuts import render

from .models import TodoList

# Create your views here.
def index(request):
    taskList = TodoList.objects.all()

    return HttpResponse(taskList.name)

def detail(request, TodoList_id):
    return HttpResponse({"You are looking at this task %s" %TodoList_id})