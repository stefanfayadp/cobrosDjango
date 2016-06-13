from __future__ import unicode_literals

from django.db import models

# Create your models here.

class trabajadores(models.Model):
    idTrabajador = models.AutoField(primary_key=True)
    cedulatr = models.CharField(max_length=20)
    nombretr = models.CharField(max_length=50)
    apellstr = models.CharField(max_length=80)
    teltr = models.CharField(max_length=20)
    direcciontr = models.CharField(max_length=30)
    tipoacc = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return str(self.idTrabajador)
