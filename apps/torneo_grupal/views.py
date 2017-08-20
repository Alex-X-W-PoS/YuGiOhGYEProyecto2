from django.shortcuts import render, redirect
from apps.torneo_grupal.models import Torneo_Grupal
from django.core import serializers
from django.http import HttpResponse
from apps.torneo_grupal.forms import TorneoGrupalForm

# Create your views here.

def listarTorneosGrupales(request):
    print('Aqui estamos')
    if request.is_ajax():
        data = Torneo_Grupal.objects.all().order_by('-fecha_hora_fin')
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')

def listarUnTorneoGrupal(request):
    if request.user.is_authenticated:
        print(request.session['rol'])
    idi = request.GET['identificacion']
    context = {}
    torneo_selec = Torneo_Grupal.objects.get(id_torneo = idi)
    id_torneo = torneo_selec.id_torneo
    nombre = torneo_selec.nombre
    fecha_hora_inicio = torneo_selec.fecha_hora_inicio
    fecha_hora_fin = torneo_selec.fecha_hora_fin
    numero_participantes_disponibles = torneo_selec.numero_participantes_disponibles
    grupo_ganador = torneo_selec.grupo_ganador
    torneo = {'id_torneo':id_torneo,'nombre': nombre,'fecha_hora_inicio':fecha_hora_inicio,'fecha_hora_fin':fecha_hora_fin,'numero_participantes_disponibles':numero_participantes_disponibles,'grupo_ganador':grupo_ganador}
    context['torneo'] = torneo
    context['rol'] = request.session['rol']
    print('Aqui estamos')
    return render(request,'landing/torneoGrupalDetalle.html',context)

def editarTorneoGrupal(request,id):
    torneo = Torneo_Grupal.objects.get(id_torneo=id)
    if request.method =='GET':
        form = TorneoGrupalForm(instance=torneo)
    else:
        form = TorneoGrupalForm(request.POST, instance=torneo)
        if form.is_valid():
            form.save()
        return redirect('torneos')
    return render(request, 'landing/torneoGrupalEditar.html',{'form':form})

def eliminarTorneoGrupal(request, id):
    torneo = Torneo_Grupal.objects.get(id_torneo=id)
    if request.method == 'POST':
        torneo.delete()
        return redirect('torneos')
    return render(request, 'landing/torneoGrupalEliminar.html', {'torneo': torneo})

def crearTorneoGrupal(request):
    if request.method == 'POST':
        form = TorneoGrupalForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('torneos')
    else:
        form = TorneoGrupalForm()
        return render(request, 'landing/torneoGrupalCrear.html', {'form': form})
