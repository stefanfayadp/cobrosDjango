from __future__ import unicode_literals

from django.db import models

# Create your models here.

class clientes(models.Model):
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apells = models.CharField(max_length=80)
    tel = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return self.cedula
