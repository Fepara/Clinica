from django.shortcuts import render, redirect
from .models import Atendimento
from .forms import AtendimentoForm

def listar_atendimentos(request):
    atendimentos = Atendimento.objects.all()
    return render(request, 'atendimento/listar_atendimentos.html', {'atendimentos': atendimentos})

def criar_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_atendimentos')
    else:
        form = AtendimentoForm()
    return render(request, 'atendimento/criar_atendimento.html', {'form': form})
