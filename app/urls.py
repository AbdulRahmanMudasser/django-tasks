from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    # Admin Panel URL
    path('admin/', admin.site.urls),
    
    # Task List URL
    path('', views.task_list, name='task_list'),
    
    # Create Task URL
    path('create/', views.task_create, name='task_create'),
    
    # Update Task URL
    path('update/<int:pk>', views.task_update, name='task_update'),
]
