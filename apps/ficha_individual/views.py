from django.shortcuts import render, redirect
from apps.ficha_individual.models import Ficha_Individual
from apps.ficha_individual.forms import FichaIndividualForm
from apps.ygoapp.models import Usuario
from apps.torneo.models import Torneo_Individual
from apps.jugador.models import Duelista
from django.http import HttpResponse

# Create your views here.

def crearFichaIndividual(request,id):
    if request.method == 'POST':
        form = FichaIndividualForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            torneo = Torneo_Individual.objects.get(id_torneo=id)
            torneo.numero_participantes_disponibles -=1
            torneo.save()
            return redirect('inscripcionExitosa')
    else:
        torneo = Torneo_Individual.objects.get(id_torneo=id)
        context = {}
        user_log = Usuario.objects.get(user_id=request.session['id'])
        nombre = user_log.usuario.username
        nombre_torneo= torneo.nombre
        duelista = Duelista.objects.get(usuario = user_log)
        data = {'torneo': torneo, 'duelista': duelista,}
        form = FichaIndividualForm(initial=data)
        context['form'] = form
        context['username'] = nombre
        context['torneo'] = nombre_torneo
        return render(request, 'landing/fichaIndividualCrear.html',context)
