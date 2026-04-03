from rest_framework import serializers
from .models import Funcionario, Tecnologia

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ['id', 'nombre']

class FuncionarioSerializer(serializers.ModelSerializer):
    # Esto hará que en el JSON veamos los nombres de las tecnologías, no solo el ID
    tecnologias = TecnologiaSerializer(many=True, read_only=True)

    class Meta:
        model = Funcionario
        fields = [
            'id', 
            'nombre_completo', 
            'rut', 
            'grado', 
            'tecnologias', 
            'fecha_ingreso', 
            'activo'
        ]