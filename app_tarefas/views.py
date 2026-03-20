from django.shortcuts import render
from .models import Tarefa

# Create your views here.
def listar_tarefas(request):
    minhas_tarefas = Tarefa.objects.all()
    
    contexto = {
        'tarefas' : minhas_tarefas
    }

    return render(request, 'lista.html', contexto)

def criar_tarefa(request):
    return render(request, 'nova.html')