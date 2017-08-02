# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.torneo_grupal.models import Torneo_Grupal
from apps.grupo.models import Grupo

# Create your models here.

Decks =(('zoodiac', 'zoodiac'),
        ('trueDraco', 'trueDraco'),
        ('trueDino', 'trueDino'),
        ('inovked', 'invoked'),
        ('infernoid', 'infernoid'),
        ('abc', 'abc'),
        ('otros', 'otros'))

class Ficha_Grupal(models.Model):
    id_ficha = models.CharField(primary_key = True,max_length=10)
    torneo = models.ForeignKey(Torneo_Grupal,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    jugador1 = models.CharField(max_length=40)
    deck1 = models.CharField(max_length=30, choices=Decks, default='otros')
    jugador2 = models.CharField(max_length=40)
    deck2 = models.CharField(max_length=30, choices=Decks, default='otros')
    jugador3 = models.CharField(max_length=40, null=True)
    deck3 = models.CharField(max_length=30, choices=Decks, default='otros',null=True)
    
    class Meta:
        db_table = 'ficha_grupal'
