from django.db import models
from pacientes.models import Paciente
from profissionais.models import Profissional

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.paciente.nome} - {self.data} {self.hora_inicio}'

    class Meta:
        unique_together = ['profissional', 'data', 'hora_inicio', 'hora_fim']
