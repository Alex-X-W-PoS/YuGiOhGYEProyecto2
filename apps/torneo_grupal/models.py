# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Torneo_Grupal(models.Model):
    id_torneo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    numero_participantes_disponibles = models.IntegerField()
    grupo_ganador = models.CharField(max_length=50,default='No hay')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'torneo_grupal'
