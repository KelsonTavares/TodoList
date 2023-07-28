from django.contrib import admin
from .models import Task, Event, Profile
# Register your models here.

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Event)