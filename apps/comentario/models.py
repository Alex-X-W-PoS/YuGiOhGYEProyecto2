# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.ygoapp.models import Usuario

# Create your models here.

class Tema(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=60)
    fecha = models.DateField()

    class Meta:
        db_table = 'tema'

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'comentario'


