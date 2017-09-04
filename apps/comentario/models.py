# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.ygoapp.models import Usuario

# Create your models here.

class Tema(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length = 100,null =False)
    descripcion = models.TextField(max_length =999)
    fecha = models.DateField(auto_now=True)

    class Meta:
        db_table = 'tema'

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'comentario'

