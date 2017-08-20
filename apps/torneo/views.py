# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from apps.torneo.models import Torneo_Individual
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def torneos(request):
    if request.user.is_authenticated:
        print(request.session['rol'])
        if request.session['rol']=='moderador':
            return render(request,'landing/torneos.html',{'mod': True})
        else:
            return render(request,'landing/torneos.html',{'mod': False})
    return render(request,'landing/torneos.html',{'mod': False})

def listarTorneosIndividuales(request):
    print('Aqui estamos')
    if request.is_ajax():
        data = Torneo_Individual.objects.all().order_by('-fecha_hora_fin')
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')
