# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygoapp', '0003_auto_20170819_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('administrador', 'administrador'), ('moderador', 'moderador'), ('jugador', 'jugador')], default='jugador', max_length=30),
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
