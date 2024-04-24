"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from storage.views import get_floors, get_rooms
from users.views import login_view, logout_view
urlpatterns = [
    path('logout/', logout_view, name='logout' ),
    path('login/', login_view, name='login' ),
    path('get_floors/', get_floors, name='get_floors'),
    path('get_rooms/', get_rooms, name='get_rooms'),
    path('storage/', include('storage.urls')),
    path('admin/', admin.site.urls),
]
