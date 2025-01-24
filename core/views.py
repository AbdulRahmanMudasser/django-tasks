from django.shortcuts import render, redirect, get_object_or_404
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

# Create Task View
def task_create(request):
    # Check if Request Method is POST
    if request.method == 'POST':
        # Get title from POST Request
        title = request.POST.get('title')
        
        # Get description from POST Request
        description = request.POST.get('description')
        
        # Create Task
        models.Task.objects.create(title=title, description=description)
        
        # Redirect to Task List Template
        return redirect('task_list')
    
    # Render Task Create Template
    return render(request, 'core/task_form.html')

# Update Task View
def task_update(request, pk):
    # Get Task With pk
    task = get_object_or_404(models.Task, pk=pk)
    
    # Check if Request Method is POST
    if request.method == 'POST':
        # Get Updated title from POST Request
        task.title = request.POST.get('title')
        
        # Get Updated description from POST Request
        task.description = request.POST.get('description', '')
        
        # Get Task Completion status from POST Request
        task.completed = 'completed' in request.POST
        
        # Save Task
        task.save()
        
        # Redirect to Task List Template
        return redirect('task_list')
    
    context = {
        'task': task,
    }
    
    # Render Task Update Template
    return render(request, 'core/task_form.html', context)
