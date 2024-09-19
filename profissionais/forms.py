from django import forms
from .models import Profissional

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'especialidade', 'telefone', 'email', 'registro_profissional']
