from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import constants
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from .form import TaskForm, UserForm
from .models import Task, Event, Profile
import datetime

# Create your views here.

def index(request):
    #return HttpResponse('<h1>Ola Minhas Tarefas!</h1>')
    data = {}
    data['tasks'] = Task.objects.all()
    data['users'] = User.objects.all()
    #dados = ['Correr','Desporto','Esse e uma actividade muito dinamica e saudavel']
    return render(request, 'tasks/index.html',data)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'tasks/signup.html', {'form': form})

def signin(request):
    pass