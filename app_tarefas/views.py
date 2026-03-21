from django.shortcuts import render,redirect
from .models import Tarefa

# Create your views here.
def lista_tarefas(request):
   
    if request.method == "POST":
       
        texto_digitado = request.POST.get('novo_titulo')
        
        Tarefa.objects.create(titulo=texto_digitado)
        
        return redirect('home')
    
    minhas_tarefas = Tarefa.objects.all()
    return render(request, 'lista.html', {'tarefas' : 
minhas_tarefas})

def concluir_tarefa(request, tarefa_id):

    tarefa = Tarefa.objects.get(id=tarefa_id)

    tarefa.concluida = True

    tarefa.save()

    return redirect('home')

def deletar_tarefa(request, tarefa_id):

    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect('home')


    
   

