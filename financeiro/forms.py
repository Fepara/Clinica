from django import forms
from .models import Pagamento, Despesa, Receita

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['paciente', 'valor', 'data_pagamento', 'descricao']
        labels = {
            'descricao': 'Descrição',
        }

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data_despesa']
        labels = {
            'descricao': 'Descrição',
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data_receita']
        labels = {
            'descricao': 'Descrição',
        }
