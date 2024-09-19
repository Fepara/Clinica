from django.shortcuts import render, redirect
from .models import Agendamento
from .forms import AgendamentoForm

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agendamentos/listar_agendamentos.html', {'agendamentos': agendamentos})

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamentos/criar_agendamento.html', {'form': form})
