# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image

# Create your models here.

TIPO =(('sobre_expansion', 'sobre_expansion'),
       ('lata', 'lata'),
       ('caja_ed_especial', 'caja_ed_especial'),
       ('sobre_duelista','sobre_duelista'),
       ('baraja_principiante','baraja_principiante'),
       ('baraja_estructura','baraja_estructura'))

class Producto(models.Model):
    codigo = models.CharField(primary_key=True,max_length=4)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=TIPO, default='sobre_expansion')
    fecha_salida = models.DateField()
    url = models.TextField()

    class Meta:
        db_table = 'producto'
