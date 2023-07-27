from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import forms
from .models import Task, Event, Profile

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=300)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password']