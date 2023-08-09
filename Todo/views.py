from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from .forms import TaskForm, UserForm, ProfileForm, EventForm
from .models import Task, Event, Profile
from notifications.signals import notify
# import datetime

# Create your views here.
@login_required(login_url='signin')
def index(request):
    data = {}
    data['tasks'] = Task.objects.all()
    data['profile'] = Profile.objects.all()
    data['events'] = Event.objects.all()
    data['page'] = 'index'
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
                return redirect('signin')
            else:
                messages.error(request,'Passwords are not same!')
                redirect('signup')
        else:
            messages.error(request,'The data are not ok!')
            
    else:
        form = UserForm()
    return render(request, 'Todo/forms.html', {'form': form, 'page':page})

def signin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')# Aqui pega o username no request
        password = request.POST.get('password')# Aqui pega a password no request
        
        try:
            user = User.objects.filter(username = username)
            # Pega os dados do usuario atraves do seu username e
            # verifica se o usuario existe na base de dados.
        except:
            messages.error(request,'User does not exist')
            
        user = authenticate(request, username=username, password=password) # Aqui faz a autenticacao do usuario.

        if user is not None: # Aqui verifica se os dados do usuario estao vaizios ou nao
            login(request, user)# Faz o login
            messages.success(request,'Signin with sucess!')
            return redirect('index')
        else:
            messages.error(request, 'Username or Password does not exist')
              
    return render(request, 'Todo/forms.html',{'page':page})

def logoutUser(request): # logout method
    logout(request) # Faz o logout
    return redirect('signin')

@login_required(login_url='signin')
def createTask(request):
    page = "create"
    user = User.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Success in creating Task!')
            return redirect('index')
        else:
            messages.error(request,'The data are not ok!')
    return render(request, 'tasks/forms.html',{'users':user, 'page':page})

@login_required(login_url='signin')
def updateTask(request,pk):
    page = "edit"
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance = task)
    
    if request.user.profile != task.owner:
        messages.info(request,'Your are not allowed here!')
    else:
        if request.method == 'POST': # Aqui verifica se o methodo usado no form e post
            form = TaskForm(request.POST, instance = task)
            if form.is_valid():# Aqui verifica se o form e valido
                form.save()
                messages.success(request,'Success in updating task!')
                return redirect('index')
    return render(request, 'tasks/forms.html', {'task':task, 'page':page})

@login_required(login_url='signin')
def deleteTask(request, pk):
    task = Task.objects.get(pk = pk)
    if request.method == 'POST':
        task.delete()
        messages.info(request,'task! deleted!')
        return redirect('index')
    
    return render(request, 'index.html', {'task':task})

@login_required(login_url='signin')
def profile(request):
    page = "create"
    if request.method == "POST":
        # prof = Profile.objects.get(user = request.user)
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile was created!')
            return redirect('index')
        else:
            messages.error(request,'The data are not ok!')
        
    return render(request, 'todo/profile.html', {'page' : page})

@login_required(login_url='signin')
def EditProfile(request, pk):
    page = "edit"
    prof = Profile.objects.get(pk = pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = prof)
        if form.is_valid():
            form.save()
            messages.success(request,'Success in updating your Profile!')
            return redirect('index')
        else:
            messages.error(request,'The data are not ok!')
            
    return render(request, 'todo/profile.html', {'profile' : prof, 'page' : page})

@login_required(login_url='signin')
def Show_P(request):
    profile = Profile.objects.get(pk = request.user.profile)
    # key = request.user.password
    # c = Cipher(algorithms.AES(key), modes.CTR(key[:len(key)-1]))
    return render(request, 'Todo/profile.html',{'profile' : profile})

@login_required(login_url='signin')
def createEvent(request, pk):
    page = 'create'
    task = Task.objects.get(pk = pk)
    # event = Event.objects.get(pk = task.event.id)
    # if event:
    #     messages.info(request, 'This task already has an event!')
    #     return redirect('index')
        
    if request.method == "POST":
        form = EventForm({
            'name' : request.POST['name'],
            'task' : request.POST['task'],
            'alarm' : request.POST['alarm']
        })
        
        if form.is_valid():
            form.save()
            messages.success(request,'Event was created!')
            return redirect('index')
        else:
            messages.error(request,'The data are not ok!')
        
    return render(request, 'event/form.html',{'task' : task, 'page':page})

@login_required(login_url='signin')
def updateEvent(request, pk):
    page = 'edit'
    event = Event.objects.get(pk = pk)
    
    if request.method == "POST":
        form = EventForm(request.POST, instance = event)
        if form.is_valid():
            form.save()
            messages.success(request,'Success in updating event!')
            return redirect('index')
        else:
            messages.error(request,'The data are not ok!')
            
    return render(request, 'index.html', {'event' : event, 'page' : page})

@login_required(login_url='signin')
def deleteEvent(request, pk):
    event = Event.objects.get(pk = pk)
    if request.method == "POST":
        event.delete()
        messages.info(request,'Event was deleted!')
        return redirect('index')
    
    return render(request, 'index.html',{'event':event})

@login_required(login_url='signin')
def about(request):
    return render(request, 'Todo/about.html')


@login_required(login_url='signin')
def notification(request):
    try:
        if request.method == 'POST':
            event = Event.objects.all()
            receiver = User.objects.get(id=request.user.id)
            for eve in event:
                if int(eve.alarm[:2]) == 10:
                    notify.send(eve, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('index')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
    return render(request, 'index.html')