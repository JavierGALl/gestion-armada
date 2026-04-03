from rest_framework import viewsets, filters
from .models import Funcionario, Tecnologia
from .serializers import FuncionarioSerializer, TecnologiaSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_completo', 'rut']

class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer