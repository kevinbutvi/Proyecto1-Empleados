from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shot_name = models.CharField('Nombre_Corto', max_length=20)
    anulate = models.BooleanField('anulado', default = False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ["id"]

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.shot_name
