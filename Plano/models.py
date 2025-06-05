from django.db import models
from Cliente.models import Cliente
# Create your models here.
class Plano(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.TextField()

class Plano_Cliente(models.Model):
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_assinatura = models.DateTimeField(auto_now_add=True)
    data_cancelamento = models.DateTimeField(blank=True, null=True)
    data_vencimento = models.DateTimeField()
    status = models.BooleanField(default=True)