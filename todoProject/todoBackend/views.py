from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import TodoList
from .forms.taskForm import AddTask

# Create your views here.
def index(request):
    taskList = TodoList.objects.all()
    context = {
        'taskList':taskList
    }

    return render(request, 'tasks/index.html', context )

def detail(request, TodoList_id):
    task = get_object_or_404(TodoList, pk=TodoList_id)

    return render(request, 'tasks/detail.html', {'task':task})

def edit(request, TodoList_id):
    task = get_object_or_404(TodoList, pk=TodoList_id)

    task.description = request.POST['description.value']

    # task.save()

    return render(request, 'tasks/detail.html', {'task':task})
    # return HttpResponseRedirect(reverse('todoBackend:edit', args=(task.id,)))