from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Nivel_Acesso(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    autoridade = models.IntegerField()

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    vinculo = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    nivel_acesso = models.ForeignKey(Nivel_Acesso, on_delete=models.CASCADE)

    def __str__(self):
        return self.vinculo.first_name