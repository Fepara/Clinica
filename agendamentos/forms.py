from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['paciente', 'profissional', 'data', 'hora_inicio', 'hora_fim', 'observacoes']
        labels = {
            'observacoes': 'Observações',
        }
