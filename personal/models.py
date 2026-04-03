from django.db import models

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tecnologías"

class Funcionario(models.Model):
    nombre_completo = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    grado = models.CharField(max_length=50, help_text="Ej: Sargento, Teniente, Civil")

    tecnologias = models.ManyToManyField(Tecnologia, related_name="expertos")
    
    fecha_ingreso = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.grado} - {self.nombre_completo}"