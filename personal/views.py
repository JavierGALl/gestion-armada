from django.shortcuts import render
from rest_framework import viewsets
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework import filters

class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    Esta vista provee automáticamente acciones de 'list', 'create', 'retrieve',
    'update' y 'destroy'.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    # AGREGA ESTAS DOS LÍNEAS:
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_completo', 'rut']