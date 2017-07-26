# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ygoapp.models import Usuario
from grupo.models import Grupo

# Create your models here.
Decks =(('zoodiac', 'zoodiac'),
        ('trueDraco', 'trueDraco'),
        ('trueDino', 'trueDino'),
        ('inovked', 'invoked'),
        ('infernoid', 'infernoid'),
        ('abc', 'abc'),
        ('otros', 'otros'))

class Jugador(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, unique=True)
	deck = models.CharField(max_length=30, choices=Decks, default='otros')
	is_into_the_vrains = models.BooleanField(_('esta_conectado'), default=False, blank=False)
	grupo = models.ManyToManyField(Grupo)

