from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models

# Sign Up User View
def signup(request):
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
        user = User.objects.create_user(username_, password)
        
        # Save User
        user.save()
        
        # Redirect to Login Page]
        return redirect('/login')
    
    # Render Sign Up Page
    return render(request, 'signup.html')

# Login User View
def login(request):
    # Render Login Page
    return render(request, 'login.html')
