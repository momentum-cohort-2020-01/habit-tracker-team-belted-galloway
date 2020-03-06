from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Habit, Unit, DailyLog
from .forms import HabitForm


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_list.html', {'habits': habits})


def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'core/habit_detail.html', {'habit': habit, 'pk': pk})


def new_habit(request, pk):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit-list', pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, 'core/new_habit.html', {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit-detail', pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'form': form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit-list')        
