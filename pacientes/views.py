from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/cadastrar_paciente.html', {'form': form})
