#from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import User
from .models import Task, Event, Profile

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender','birth']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','summary','category', 'owner']
