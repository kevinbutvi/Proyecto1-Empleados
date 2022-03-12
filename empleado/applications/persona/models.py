from email.policy import default
from re import T
from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name = "Hablidad"
        verbose_name_plural = "Habilidades Empleados"

    def __str__(self):
        return str(self.id) + "--" + self.habilidad



class Empleado(models.Model):
    """ Modelo para Tabla Empleado"""
    job_choices = (
            ("1", "CONTADOR"),
            ("2", "ADMINISTRADOR"),
            ("3", "ECONOMISTA"),
            ("4", "OTRO"))
    
    first_name = models.CharField("Nombre", max_length=60)
    last_name = models.CharField("Apellidos", max_length=50)
    full_name = models.CharField("Nombre Completo", max_length=120, blank=True)
    job = models.CharField("Trabajo", choices=job_choices, max_length=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField("Imagen", upload_to="empleado", blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personal'
        ordering = ["first_name" , "last_name"]


    def __str__(self):
        return str(self.id) + "--" + self.first_name + "--" + self.last_name