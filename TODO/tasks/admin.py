from django.contrib import admin
from .models import User, Tasks, Category, Login
# Register your models here.

admin.site.register(User)
admin.site.register(Login)
admin.site.register(Tasks)
admin.site.register(Category)
