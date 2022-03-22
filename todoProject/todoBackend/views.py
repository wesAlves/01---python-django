from django.shortcuts import render

from .models import TodoList

# Create your views here.
def index(request):
    taskList = TodoList.objects.all()
    context = {
        'taskList':taskList
    }

    return render(request, 'tasks/index.html', context )

def detail(request, TodoList_id):
    context = {"taskList": ""}

    return render(request, 'tasks/index.html', context)