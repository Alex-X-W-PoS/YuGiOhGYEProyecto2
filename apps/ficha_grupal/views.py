from django.shortcuts import render, redirect
from apps.ficha_grupal.models import Ficha_Grupal
from apps.ficha_grupal.forms import SeleccionarGrupoForm, FichaGrupalForm
from apps.ygoapp.models import Usuario
from apps.torneo_grupal.models import Torneo_Grupal
from apps.jugador.models import Duelista
from apps.grupo.models import Grupo
from django.http import HttpResponse

# Create your views here.

def crearFichaGrupal(request,id):
    torneo = Torneo_Grupal.objects.get(id_torneo=id)
    if request.method == 'POST':
        user_log = Usuario.objects.get(user_id=request.session['id'])
        duelista = Duelista.objects.get(usuario = user_log)
        form = SeleccionarGrupoForm(duelista,request.POST)
        print(form.is_valid())
        if form.is_valid():
            context = {}
            idg = request.POST.get('grupo')
            nombre_torneo= torneo.nombre
            grupo = Grupo.objects.get(group_id = idg)
            data = {'torneo': torneo,'grupo':grupo,}
            form = FichaGrupalForm(grupo,initial = data)
            context['form']=form
            context['torneo'] = nombre_torneo
            context['grupo'] = grupo.nombre
            return render(request, 'landing/fichaGrupalCrearPaso2.html',context)
            
    else:
        context = {}
        user_log = Usuario.objects.get(user_id=request.session['id'])
        nombre_torneo= torneo.nombre
        duelista = Duelista.objects.get(usuario = user_log)
        data = {'torneo': torneo,}
        form = SeleccionarGrupoForm(duelista,initial=data)
        context['form'] = form
        context['torneo'] = nombre_torneo
        return render(request, 'landing/fichaGrupalCrear.html',context)

def ingresarFichaGrupal(request):
    if request.method == 'POST':
        idg = request.POST.get('grupo')
        grupo = Grupo.objects.get(group_id = idg)
        form = FichaGrupalForm(grupo,request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            form.save()
            idt = request.POST.get('torneo')
            torneo = Torneo_Grupal.objects.get(id_torneo=idt)
            torneo.numero_participantes_disponibles -=1
            torneo.save()
        return redirect('inscripcionExitosa')
