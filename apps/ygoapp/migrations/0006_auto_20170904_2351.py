# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygoapp', '0005_auto_20170819_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, default='static/media/usuario/noimagen.jpg', help_text='Foto', null=True, upload_to='static/media/usuario/'),
        ),
    ]
