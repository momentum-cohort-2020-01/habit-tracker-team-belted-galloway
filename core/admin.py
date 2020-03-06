from django.contrib import admin
from .models import Habit, Unit, DailyLog

admin.site.register(Habit)
admin.site.register(Unit)
admin.site.register(DailyLog)


