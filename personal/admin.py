from django.contrib import admin
from .models import Funcionario, Tecnologia

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'grado', 'activo')
    list_filter = ('grado', 'activo')
    search_fields = ('nombre_completo', 'rut')