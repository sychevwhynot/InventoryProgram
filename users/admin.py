from django.contrib import admin
from .models import CustomUsers
from django.contrib.auth.models import Group


admin.site.register(CustomUsers)
admin.site.unregister(Group)
