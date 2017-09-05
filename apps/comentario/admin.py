# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.comentario.models import Comentario, Tema

# Register your models here.
admin.site.register(Comentario)
admin.site.register(Tema)
