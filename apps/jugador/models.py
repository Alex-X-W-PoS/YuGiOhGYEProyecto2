# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.ygoapp.models import Usuario

# Create your models here.


class Duelista(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
	is_into_the_vrains = models.BooleanField(('esta_conectado'), default=False, blank=False)

	def __str__(self):
                return self.usuario.usuario.username
        
	class Meta:
                db_table = 'jugador'

