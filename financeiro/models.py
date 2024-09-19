from django.db import models
from pacientes.models import Paciente

class Pagamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Pagamento de {self.paciente.nome} em {self.data_pagamento}'

class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_despesa = models.DateField()

    def __str__(self):
        return f'Despesa: {self.descricao} em {self.data_despesa}'

class Receita(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_receita = models.DateField()

    def __str__(self):
        return f'Receita: {self.descricao} em {self.data_receita}'
