from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    srno = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    