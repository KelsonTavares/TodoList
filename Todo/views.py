from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.messages import constants
from django.contrib import messages
# from django.urls import reverse
from django.http import HttpResponse
from .forms import TaskForm, UserForm
from .models import Task, Event, Profile
# import datetime

# Create your views here.

def index(request):
    data = {}
    data['tasks'] = Task.objects.all()
    data['users'] = User.objects.all()
    #data['passw'] = check_password('admin','X6AL5TV08PEWo5BAP/tgMx5zgd6TZsbNZ3zXcEWAJfQ=')
    #dados = ['Correr','Desporto','Esse e uma actividade muito dinamica e saudavel']
    # b = make_password('admin')
    # print(b)
    # c = check_password('admin',b)
    # print(c)
    # e = check_password('maria2002', 'pbkdf2_sha256$600000$DyGTkMHx5SJLDOE0pR9oH6$2DN13k6lQdKmYwZSDLlaCnV1jGelaJLQatkWmsjWh9I=')
    # print(e)
    # #print(data['passw'])
    #print(check_password('ravi2000', 'pbkdf2_sha256$600000$4LJV1ICvojox9atabvwgtw$B9i/BeQPPwqFan+JsqzrjaMRkCn2SuzEMi+cv6gQVvU='))
    return render(request, 'index.html',data)

def signup(request):
    page = 'signup'
    if request.method == 'POST':
        form = UserForm({
            'first_name' : request.POST['first_name'],
            'last_name' : request.POST['last_name'],
            'username' : request.POST['username'],
            'email' : request.POST['email'],
            'password' : make_password(request.POST['password']),
            })
        
        if form.is_valid():
            if request.POST['password'] == request.POST['password2']:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                print('Succes in Signup!')
                return redirect('signin')
            else:
                print('Passwords are not same!')
                redirect('signup')
        else:
            print('Form is not valid!')
            
    else:
        form = UserForm()
    return render(request, 'Todo/forms.html', {'form': form, 'page':page})

def signin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()# Aqui pega o username no request
        password = request.POST.get('password')# Aqui pega a password no request
        print(username)
        print(password)
        
        try:
            user = User.objects.filter(username = username)
            # Pega os dados do usuario atraves do seu username e
            # verifica se o usuario existe na base de dados.
        except:
            messages.error(request,'User does not exist')
            print('User does not exist')
            
        user = authenticate(request, username=username, password=password) # Aqui faz a autenticacao do usuario.
        print(user)
        if user is not None: # Aqui verifica se os dados do usuario estao vaizios ou nao
            login(request, user)# Faz o login
            print('Logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Username or Password does not exist')
            print('Username or Password does not exist')
              
    return render(request, 'Todo/forms.html',{'page':page})

def logoutUser(request): # logout method
    logout(request) # Faz o logout
    return redirect('signin')