from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Habit, DailyLog
from django.contrib.auth.models import User

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'goal',)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')