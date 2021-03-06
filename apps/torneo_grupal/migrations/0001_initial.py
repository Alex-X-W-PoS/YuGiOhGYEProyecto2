# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torneo_Grupal',
            fields=[
                ('id_torneo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_hora_inicio', models.DateTimeField()),
                ('fecha_hora_fin', models.DateTimeField()),
                ('participantes_por_grupo', models.IntegerField()),
                ('ganador', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'torneo_grupal',
            },
        ),
    ]
