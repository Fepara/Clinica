from django.shortcuts import render, redirect
from .models import Profissional
from .forms import ProfissionalForm

def listar_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'profissionais/listar_profissionais.html', {'profissionais': profissionais})

def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profissionais')
    else:
        form = ProfissionalForm()
    return render(request, 'profissionais/cadastrar_profissional.html', {'form': form})
