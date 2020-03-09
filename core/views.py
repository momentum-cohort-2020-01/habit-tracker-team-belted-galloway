from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Habit, Unit, DailyLog, User
from .forms import HabitForm, DailyLogForm

@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_list.html', {'habits': habits})


def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    habits = Habit.objects.all()
    logs = DailyLog.objects.filter(habit=habit)
    return render(request, 'core/habit_detail.html', {'habit': habit, 'habits': habits, 'pk': pk, 'logs': logs})


def new_habit(request):
    habit = Habit.objects.all()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit-list')
    else:
        form = HabitForm()
    return render(request, 'core/new_habit.html', {'form': form, 'habit': habit})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habits = Habit.objects.all()
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit-list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'form': form, 'habits': habits, 'pk':pk})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('habit-list')        

def track_habit(request, pk):
    habits = Habit.objects.all()
    habit = get_object_or_404(Habit, pk=pk)
    log = DailyLog(habit=habit)
    if request.method == "POST":
        form = DailyLogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save()
            return redirect('habit-list')
    else:
        form = DailyLogForm(instance=log)
    return render(request, 'core/track_habit.html', {'form': form, 'log': log, 'habits': habits})



def edit_log(request, pk):
    log = get_object_or_404(DailyLog, pk=pk)
    habits = Habit.objects.all()
    if request.method == 'POST':
        form = DailyLogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save()
            return redirect('habit-list')
    else:
        form = DailyLogForm(insance=log)
    return render(request, 'core/edit_log.html', {'form': form, 'log': log, 'habits': habits})


def delete_log(request, pk):
    log = get_object_or_404(DailyLog, pk=pk)
    log.delete()
    return redirect('habit-list')

