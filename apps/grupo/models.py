# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from apps.jugador.models import Duelista
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO
from datetime import date

# Create your models here.

class Grupo(models.Model):
    group_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fecha_creacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'apps/static/media/grupo/',
                             default = 'apps/static/media/grupo/noimagen.jpg', null=True,
                             blank=True, editable=True,
                             help_text="Foto")
    torneos_ganados = models.IntegerField(default=0)
    duelistas = models.ManyToManyField(Duelista, null=True, blank=True, default=None)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'grupo'
