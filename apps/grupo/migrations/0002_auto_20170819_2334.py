# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='imagen',
            field=models.ImageField(blank=True, default='apps/static/media/grupo/noimagen.jpg', help_text='Foto', null=True, upload_to='apps/static/media/grupo/'),
        ),
    ]
