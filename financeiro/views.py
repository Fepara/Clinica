from django.shortcuts import render, redirect
from .models import Pagamento, Despesa, Receita
from .forms import PagamentoForm, DespesaForm, ReceitaForm

# Pagamentos
def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'financeiro/listar_pagamentos.html', {'pagamentos': pagamentos})

def criar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pagamentos')
    else:
        form = PagamentoForm()
    return render(request, 'financeiro/criar_pagamento.html', {'form': form})

# Despesas
def listar_despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'financeiro/listar_despesas.html', {'despesas': despesas})

def criar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm()
    return render(request, 'financeiro/criar_despesa.html', {'form': form})

# Receitas
def listar_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'financeiro/listar_receitas.html', {'receitas': receitas})

def criar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_receitas')
    else:
        form = ReceitaForm()
    return render(request, 'financeiro/criar_receita.html', {'form': form})
