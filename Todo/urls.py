from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('task/', views.createTask, name='task'),
    path('task/edit/<str:pk>/', views.updateTask, name='updateTask'),
    path('task/delete/<str:pk>/', views.deleteTask, name='deleteTask'),
    
    path('event/<str:pk>/', views.createEvent, name='createEvent'),
    path('event/delete/<str:pk>/', views.deleteEvent, name='deleteEvent'),
    path('event/edit/<str:pk>/', views.updateEvent, name='updateEvent'),
    
    path('profile/', views.profile, name='profile'),
]
    