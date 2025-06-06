from rest_framework.routers import DefaultRouter
from .views import ClienteModelViewSet

cliente_rota = DefaultRouter()
cliente_rota.register(r'clientes', ClienteModelViewSet, basename='clientes')