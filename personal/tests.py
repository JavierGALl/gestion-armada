from django.test import TestCase
from .models import Funcionario, Tecnologia

class FuncionarioModelTest(TestCase):
    def setUp(self):
        self.tech = Tecnologia.objects.create(nombre="Python")
        self.funcionario = Funcionario.objects.create(
            nombre_completo="Test User",
            rut="11.111.111-1",
            grado="Cabo"
        )
        self.funcionario.tecnologias.add(self.tech)

    def test_creacion_funcionario(self):
        """Verifica que el funcionario se guardó correctamente"""
        f = Funcionario.objects.get(nombre_completo="Test User")
        self.assertEqual(f.grado, "Cabo")
        self.assertEqual(f.tecnologias.count(), 1)

    def test_str_representation(self):
        self.assertEqual(str(self.funcionario), "Cabo - Test User")