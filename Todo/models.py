from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Gender_CHOICES = [ ('M', 'Masculine'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=Gender_CHOICES, null=False)
    birth = models.DateField(null=False)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    class Meta:
        verbose_name_plural = 'Profiles'
        
class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)
    summary = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tasks'
        

class Event(models.Model):
    name = models.CharField(max_length=100, null=False)
    task = models.OneToOneField(Task, on_delete=models.CASCADE, null=False)
    alarm = models.CharField(max_length=5, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Events'