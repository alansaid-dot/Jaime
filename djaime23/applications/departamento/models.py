from django.db import models

class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    subnombre = models.CharField('Nombre_Corto', max_length=20, unique=True)
    activo = models.BooleanField('Activo', default=True)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nombre']
        unique_together=('nombre', 'subnombre')
    
    def __str__(self):
        return self.nombre + '-' + self.subnombre