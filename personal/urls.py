from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet

# El Router crea las rutas /api/funcionarios/ automáticamente
router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]