from django.db import models
from agendamentos.models import Agendamento

class Atendimento(models.Model):
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
    notas = models.TextField()
    data_atendimento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Atendimento de {self.agendamento.paciente.nome} em {self.data_atendimento}'
