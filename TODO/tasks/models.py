from datetime import datetime
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Gender_CHOICES = [ ('M', 'Masculine'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=Gender_CHOICES)
    birth = models.DateField()
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Users'
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categorys'

class Tasks(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tasks'
        

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user