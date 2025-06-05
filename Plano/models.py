from django.db import models

# Create your models here.
class Plano(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.TextField()