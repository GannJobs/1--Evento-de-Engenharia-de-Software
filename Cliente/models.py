from django.db import models
from django.contrib.auth.models import User
from Plano.models import Plano_Cliente
# Create your models here.
class Pais(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cep = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade.nome}"

class Cliente(models.Model):
    # User: username, email, password, fitst_name (utilziar como nome completo)
    vinculo = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    plano_cliente = models.ForeignKey(Plano_Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.vinculo.first_name
