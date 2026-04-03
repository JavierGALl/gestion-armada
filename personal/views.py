from django.shortcuts import render
from rest_framework import viewsets
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework import filters

class FuncionarioViewSet(viewsets.ModelViewSet):

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_completo', 'rut']