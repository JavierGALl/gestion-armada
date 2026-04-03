from rest_framework import serializers
from .models import Funcionario, Tecnologia

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ['id', 'nombre']

class FuncionarioSerializer(serializers.ModelSerializer):
    # 'queryset' permite que enviemos IDs al crear/editar
    # 'many=True' porque un funcionario tiene varias tecnologías
    tecnologias_detalle = TecnologiaSerializer(source='tecnologias', many=True, read_only=True)
    tecnologias = serializers.PrimaryKeyRelatedField(
        queryset=Tecnologia.objects.all(), 
        many=True, 
        write_only=False # Permitimos lectura y escritura por ID
    )

    class Meta:
        model = Funcionario
        fields = ['id', 'nombre_completo', 'rut', 'grado', 'tecnologias', 'tecnologias_detalle', 'fecha_ingreso', 'activo']