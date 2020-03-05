"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.habit_list, name='habit-list'),
    path('habit/new/<int:pk>', views.new_habit, name='new-habit'),
    path('habit/<int:pk>/', views.habit_detail, name='habit-detail'),
    path('habit/<int:pk>/edit', views.edit_habit, name='edit-habit'),
    path('habit/<int:pk>/delete', views.delete_habit, name='delete-habit'),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns