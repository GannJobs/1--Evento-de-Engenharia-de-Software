from .models import Cliente, Endereco, Cidade, Estado, Pais
from rest_framework import serializers

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()

    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Cidade
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer()

    class Meta:
        model = Endereco
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente.vinculo.field.related_model
        fields = ['username', 'email', 'first_name']

class ClienteSerializer(serializers.ModelSerializer):
    vinculo = UserSerializer()
    endereco = EnderecoSerializer()

    class Meta:
        model = Cliente
        fields = '__all__'