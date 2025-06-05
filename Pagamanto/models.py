from django.db import models
from Cliente.models import Cliente
from Plano.models import Plano
# Create your models here.
class Forma_Pagamento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey(Forma_Pagamento, on_delete=models.CASCADE)
    data_criado = models.DateTimeField(auto_now_add=True)
    nota_fiscal = models.FileField(upload_to='notas_fiscais/', blank=True, null=True)