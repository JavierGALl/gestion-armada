from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet, TecnologiaViewSet 

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'tecnologias', TecnologiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]