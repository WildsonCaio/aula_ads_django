from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar-produto/', views.adicionar_produto, name='adicionar-produto')
]