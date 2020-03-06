import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Habit(models.Model):
    name = models.CharField(max_length=500)
    goal = models.CharField(max_length=500)
    goal_value = models.IntegerField(default =1)
    goal_unit = models.ForeignKey('Unit', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, related_name='users_habits', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'Habit Name: {self.name} Daily Goal for: {self.goal}'

    class Meta:
        ordering = ['-created_at']

class Unit(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class DailyLog(models.Model):
    activity_date = models.DateField(default=datetime.date.today)
    habit = models.ForeignKey(to=Habit, related_name='habit_log', on_delete=models.CASCADE, blank=True ,null=True)
    value = models.IntegerField(default=0)
    comments = models.TextField(max_length=None)

    def __str__(self):
        return f'Date Tracked: {self.activity_date}, Habit: {self.habit.pk}'