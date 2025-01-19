from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    
    # Todo View URL
    path('todo/', views.home, name='todo'),
]
