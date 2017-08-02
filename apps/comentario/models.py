# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.ygoapp.models import Usuario

# Create your models here.

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    
    class Meta:
        db_table = 'comentario'
