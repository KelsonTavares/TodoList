from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='url_index'),
    path('signup/', views.signup, name='signup'),
    # path('cadastro/', views.valida_cadastro, name='cadastro'),
    path('signin/', views.signin, name='signin'),
]
    