from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_tarefas, name='home'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
]