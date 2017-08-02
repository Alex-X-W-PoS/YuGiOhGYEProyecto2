# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from apps.jugador.models import Duelista

# Create your models here.

class Grupo(models.Model):
    group_id = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to = 'grupo/',
                             default = 'grupo/noimagen.jpg', null=True,
                             blank=True, editable=True,
                             help_text="Foto")
    torneos_ganados = models.IntegerField()
    duelistas = models.ManyToManyField(Duelista, null=True, blank=True, default=None)

    class Meta:
        db_table = 'grupo'
