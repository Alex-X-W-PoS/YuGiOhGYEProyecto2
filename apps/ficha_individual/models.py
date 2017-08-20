# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.torneo.models import Torneo_Individual
from apps.jugador.models import Duelista

# Create your models here.

Decks =(('zoodiac', 'zoodiac'),
        ('trueDraco', 'trueDraco'),
        ('trueDino', 'trueDino'),
        ('inovked', 'invoked'),
        ('infernoid', 'infernoid'),
        ('abc', 'abc'),
        ('otros', 'otros'))

class Ficha_Individual(models.Model):
    id_ficha = models.AutoField(primary_key = True)
    torneo = models.ForeignKey(Torneo_Individual,on_delete=models.CASCADE)
    duelista = models.ForeignKey(Duelista,on_delete = models.CASCADE)
    deck = models.CharField(max_length=30, choices=Decks, default='otros')

    class Meta:
        db_table = 'ficha_individual'
