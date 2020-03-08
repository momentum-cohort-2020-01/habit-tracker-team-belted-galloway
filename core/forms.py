from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


from .models import Habit, Unit, DailyLog
from django.contrib.auth.models import User

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('goal', 'goal_value', 'goal_unit', 'user')

class DailyLogForm(forms.ModelForm):

    class Meta:
        model = DailyLog
        fields = ('habit', 'activity_date', 'value', 'comments')