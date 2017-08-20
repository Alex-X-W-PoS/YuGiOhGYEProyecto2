# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from apps.torneo.models import Torneo_Individual
from django.core import serializers
from django.http import HttpResponse
from apps.torneo.forms import TorneoIndividualForm

# Create your views here.

def torneos(request):
    if request.user.is_authenticated:
        print(request.user.username)
        if request.session['rol']=='administrador':
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

def listarUnTorneoIndividual(request):
    if request.user.is_authenticated:
        print(request.session['rol'])
    idi = request.GET['identificacion']
    context = {}
    torneo_selec = Torneo_Individual.objects.get(id_torneo = idi)
    id_torneo = torneo_selec.id_torneo
    nombre = torneo_selec.nombre
    fecha_hora_inicio = torneo_selec.fecha_hora_inicio
    fecha_hora_fin = torneo_selec.fecha_hora_fin
    numero_participantes_disponibles = torneo_selec.numero_participantes_disponibles
    ganador = torneo_selec.ganador
    torneo = {'id_torneo':id_torneo,'nombre': nombre,'fecha_hora_inicio':fecha_hora_inicio,'fecha_hora_fin':fecha_hora_fin,'numero_participantes_disponibles':numero_participantes_disponibles,'ganador':ganador}
    context['torneo'] = torneo
    context['rol'] = request.session['rol']
    print('Aqui estamos')
    return render(request,'landing/torneoIndividualDetalle.html',context)

def editarTorneoIndividual(request,id):
    torneo = Torneo_Individual.objects.get(id_torneo=id)
    if request.method =='GET':
        form = TorneoIndividualForm(instance=torneo)
    else:
        form = TorneoIndividualForm(request.POST, instance=torneo)
        if form.is_valid():
            form.save()
        return redirect('torneos')
    return render(request, 'landing/torneoIndividualEditar.html',{'form':form})

def eliminarTorneoIndividual(request, id):
    torneo = Torneo_Individual.objects.get(id_torneo=id)
    if request.method == 'POST':
        torneo.delete()
        return redirect('torneos')
    return render(request, 'landing/torneoIndividualEliminar.html', {'torneo': torneo})

def crearTorneoIndividual(request):
    if request.method == 'POST':
        form = TorneoIndividualForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('torneos')
    else:
        form = TorneoIndividualForm()
        return render(request, 'landing/torneoIndividualCrear.html', {'form': form})
            
    
