from django.shortcuts import render, redirect
from django.contrib.auth.models import  auth, User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from .form import ProfileForm, TaskForm
from .models import Task, Profile, Event
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
    page = 'signup'
    return render(request, 'user/form_sig.html',{'page':page})

def signin(request):
    page = 'login'
    return render(request, 'user/form_sig.html',{'page':page})
# create user
# def create_user(request):
#     data = {}
#     form = ProfileForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('tasks:url_index')
#     data['form']  = form
#     return render(request, 'user/create.html', data)

# # Edit user
# def edit_user(request, id):
#     user = User.objects.get(pk=id)
#     return render(request, 'user/edit.html', {'user':user})
# # Update user datas
# def update_user(request, id):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     gender = request.POST.get('gender')
#     birth = request.POST.get('birth')
#     user = User.objects.get(pk=id)
#     user.name, user.email, user.gender, user.birth = name, email, gender, birth
#     user.save()
#     return redirect('tasks:url_index')

# def delete_user(request, id):
#     user = User.objects.get(pk=id)
#     user.delete()
#     return redirect('tasks:url_index')

# def create_task(request):
#     user = User.objects.all()
#     category = Category.objects.all()
#     form = TasksForm(request.POST or None)
    
#     if form.is_valid():
#         #form.creation_date = datetime.datetime.now()
#         form.save()
#         return redirect('tasks:url_index')
    
#     return render(request, 'tasks/create.html', {'user':user, 'category':category, 'form':form})


# def edit_task(request, id):
#     task = Tasks.objects.get(pk=id)
#     category = Category.objects.all() #get(pk=task.category.id)
#     return render(request, 'tasks/edit_task.html', {'task':task, 'category':category})

# def update_task(request, id):
#     task = Tasks.objects.get(pk=id)
#     t = task.creation_date
#     name = request.POST.get('name')
#     summary = request.POST.get('summary')
#     id = request.POST.get('category')
#     category = Category.objects.get(pk=id)#request.POST.get('category')
#     id2 = request.POST.get('owner')
#     owner = User.objects.get(pk=id2)
#     date = t
    
#     task.name, task.summary, task.category, task.creation_date, task.owner = name, summary, category, date, owner
#     task.save()
#     print(date)
#     return redirect('tasks:url_index')


# def delete_task(request, id):
#     task = Tasks.objects.get(pk=id)
#     task.delete()
#     return redirect('tasks:url_index')


# def login(request):
#     login = Login.objects.all()
    
#     if request.method == 'POST':
#         u = ''
#         p = ''
#         user = request.POST['user']
#         pw = request.POST['password']
        
#         for l in login:
            
#             if l.user == request.POST['user']:
#                 u = l.user.name
#                 p = l.password
#                 break
#             #print(f'{l.user} -> {l.password} -> {user} -> {pw} ->')
#         #print(u)
#         if u == user and p == pw:
#             return redirect('tasks:url_index')
#         else:
#             return redirect('tasks:login')
#         #log = auth.authenticate(user=user,password=pw)
        
#     else:
#         return render(request, 'user/login.html')
            

''' # {{ erros.name }}
        context = {}
        erros = {}
        
        print('Chegou Aqui!')
        #print(request.name.value)
        name = request.POST.get('name', None)
        print(name)
        # verifica se tem erro nos dados
        if name != 'Kelson Tavares':
            erros['name'] = 'O nome nao e o valor esperado'
            
        if erros:
            context['erros'] = erros'''
            
''' if log is not None:
            auth.login(request,log)
            return redirect('tasks:url_index')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('tasks:login') '''