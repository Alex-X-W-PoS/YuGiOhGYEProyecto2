# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ygoapp', '0006_auto_20170904_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, default='apps/static/media/usuario/noimagen.jpg', help_text='Foto', null=True, upload_to='apps/static/media/usuario/'),
        ),
    ]