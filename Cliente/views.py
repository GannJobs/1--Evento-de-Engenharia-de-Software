from django.shortcuts import render
from .models import Cliente
from Funcionario.models import Funcionario
from rest_framework.viewsets import ModelViewSet
from .serializer import ClienteSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ClienteModelViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user_sistema = request.user
        funcionario = Funcionario.objects.get(vinculo=user_sistema)
        
        if funcionario.nivel_acesso.autoridade < 1:
            return Response({"detail": "Acesso negado."})

        clientes = self.get_queryset()
        serializer = self.get_serializer(clientes, many=True)
        return Response({"msg": "Encontrou os usuarios", "data":serializer.data})
        
    # def create(self, request):

    #     pass

    # def update(self, request):

    #     pass

    # def destroy(self, request):

    #     pass