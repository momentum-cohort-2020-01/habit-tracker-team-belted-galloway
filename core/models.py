from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    habit = models.CharField(max_length=500)
    goal = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    