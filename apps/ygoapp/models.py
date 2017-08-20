# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO
from PIL import Image
from django.conf import settings
from django.contrib import messages

# Create your models here.

ROLES =(('administrador', 'administrador'),
        ('moderador', 'moderador'),
        ('jugador', 'jugador'))

RANKING =(('novato', 'novato'),
          ('intermedio', 'intermedio'),
          ('experto', 'experto'),
          ('moderador','moderador'),
          ('administrador','administrador'))

class Usuario(models.Model):
	user_id = models.AutoField(primary_key = True)
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	#password = models.CharField(max_length=50,blank=False, null=False)
	#nombre = models.CharField(db_column='first_name', max_length=30, blank=False, null=False)
	#apellido = models.CharField(db_column='last_name', max_length=30, blank=False, null=False)
	#email = models.EmailField(blank=False, null=False)
	avatar = models.ImageField(upload_to = 'apps/static/media/usuario/',
                             default = 'apps/static/media/usuario/noimagen.jpg', null=True,
                             blank=True, editable=True,
                             help_text="Foto")
	rol = models.CharField(max_length=30, choices=ROLES, default='jugador')
	ranking = models.CharField(max_length=50, choices=RANKING, default='novato')

	class Meta:
            db_table = 'usuario'

	


