from __future__ import unicode_literals

from django.db import models
from clientes.models import clientes
from trabajadores.models import trabajadores

# Create your models here.

class prestamos(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    idTrabajador = models.ForeignKey(trabajadores, null=True)
    cedula = models.ForeignKey(clientes, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    numdias = models.DecimalField(max_digits=2, decimal_places=0)
    valordiario = models.DecimalField(max_digits=10, decimal_places=2)
    fechainicio = models.DateField(auto_now_add=False)
    fechafin = models.DateField(auto_now_add=False)
    estado = models.CharField(max_length=10)

    def __str__(self):
        return str(self.idPrestamo)
