from django.contrib import admin
from .models import Pais, Estado, Cidade, Endereco, Cliente

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Cliente)
