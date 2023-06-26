#from django.forms import ModelForm, Form
from django import forms
from .models import User, Tasks, Login

class UserForm(forms.ModelForm):
    '''name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    gender = forms.CharField(label='Your gender', max_length=1)
    birth = forms.DateField(label='Your birth')'''
    class Meta:
        model = User
        fields = ['name','email','gender','birth']
        

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name','summary','category', 'owner','creation_date']
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['user','password']
