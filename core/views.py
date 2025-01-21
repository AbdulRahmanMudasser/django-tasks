from django.shortcuts import render
from . import models

# All Tasks View
def task_list(request):
    # Get All Tasks
    tasks = models.Task.objects.all()
    
    context = {
        'tasks': tasks,
    }
    
    # Render Task List Template
    return render(request, 'core/task_list.html', context)
