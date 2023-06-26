from django.urls import path
from . import views

app_name = 'tasks' # utiliza-se quando usamos a estrutura 'tasks:index'
urlpatterns = [
    path('', views.index, name='url_index'),
    
    # Login and Logout urls
    path('login/', views.login, name='login'),
    
    # Users url
    path('signup/', views.create_user, name='url_signup'),
    path('edit/<str:id>/', views.edit_user, name='edit_user'),
    path('update/<str:id>/', views.update_user, name='url_update'),
    path('delete/<str:id>/', views.delete_user, name='url_delete'),
    
    # Tasks url
    path('create/', views.create_task, name='create_task'),
    path('edit_task/<str:id>/', views.edit_task, name='url_edit_task'),
    path('update/<str:id>', views.update_task, name='update_task'),
    path('delete_task/<str:id>/', views.delete_task, name='url_delete_task'),
    path('<str:id>/delete/', views.delete_task, name='delete_task'),
]