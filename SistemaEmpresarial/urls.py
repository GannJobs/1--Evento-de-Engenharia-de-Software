from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView #TokenRefreshView
from Cliente.urls import cliente_rota

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(cliente_rota.urls))
]
