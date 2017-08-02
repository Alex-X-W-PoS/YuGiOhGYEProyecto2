# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Torneo_Individual(models.Model):
    id_torneo = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=30)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    ganador = models.CharField(max_length=50)

    class Meta:
        db_table = 'torneo_individual'
