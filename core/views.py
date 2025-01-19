from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import models

# Sign Up User View
def signup_user(request):
    # Check if Request Method is POST
    if request.method == 'POST':
        # Get Username from POST Method
        username_ = request.POST.get('username')
        
        # Get Email from POST Method
        email = request.POST.get('email')
        
        # Get Password from POST Method
        password = request.POST.get('password')
        
        # Print User Details
        print(username_, email, password)
        
        # Create New User
        user = User.objects.create_user(username=username_, password=password)
        
        # Save User
        user.save()
        
        # Redirect to Login Page]
        return redirect('/login')
    
    # Render Sign Up Page
    return render(request, 'signup.html')

# Login User View
def login_user(request):
    if request.method == 'POST':
        # Get Username from POST Method
        username_ = request.POST.get('username')
        
        # Get Password from POST Method
        password = request.POST.get('password')
        
        # Print User Details
        print(username_, password)
        
        # Authenticate User
        user_ = authenticate(request, username=username_, password=password)
        
        # Check if User is Not Empty
        if user_ is not None:
            # Login User
            login(request, user_)
            
            context = {
                'user': user_
            }
            
            # Redirect to Home Page
            return redirect('/home', context)
        
        else:
            # Redirect to Login Page
            return redirect('/login')
    
    # Render Login Page
    return render(request, 'login.html')

# Home View
def home(request):
    # Check if Request Method is POST
    if request.method == 'POST':
        # Get Task from POST Method
        title = request.POST.get('title')
        
        # Create Todo Model
        todo = models.Todo(title=title, user=request.user)
        
        # Save Todo
        todo.save()
        
        # Filtering Todos By Date
        todos = models.Todo.objects.filter(user=request.user).order_by('-date')
        
        context = {
            'todos': todos,
        } 
        
        # Redirect to Home Page
        return redirect('/home', context)
    
    # Filtering Todos By Date
    todos = models.Todo.objects.filter(user=request.user).order_by('-date')
        
    context = {
        'todos': todos,
    } 
    
    # Render Home Page
    return render(request, 'home.html', context)
    