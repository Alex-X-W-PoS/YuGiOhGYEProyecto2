# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image
from apps.producto.models import Producto

# Create your models here.

class Carta(models.Model):
    codigo = models.CharField(primary_key=True,max_length=10)
    url = models.TextField()
    producto = models.ManyToManyField(Producto, null=False)

    class Meta:
        db_table = 'carta'
