# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from apps.ygoapp.forms import UsuarioForm, UserForm
from apps.ygoapp.models import Usuario
from apps.jugador.models import Duelista
from apps.grupo.models import Grupo
from apps.grupo.forms import GrupoForm
from apps.ficha_individual.models import Ficha_Individual
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static
from apps.ficha_individual.forms import FichaIndividualForm
from apps.torneo.models import Torneo_Individual
# Create your views here.

def crearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'landing/landing.html',{})
    else:
        form = UsuarioForm()
        return render(request,'landing/AgregarProducto.html',{'form': form})

def mostrarPerfil(request):
    rol = request.session['rol']
    user_logged=request.user
    user=Usuario.objects.get(usuario=user_logged)
    return render(request, 'landing/duelistaPerfil.html',{'user':user_logged, 'user2':user,  'rol': rol})


def editarPerfil(request):
    user_logged=request.user
    usuario=Usuario.objects.get(usuario = user_logged)
    rol = request.session['rol']
    if request.method=='GET':
        form= UsuarioForm(instance=usuario)
        form2= UserForm(instance=user_logged)
        #print(form)
    else:
        form=UsuarioForm(request.POST, instance=usuario)
        form2=UserForm(request.POST, instance=user_logged)
        #print(form)
        print(form2)
        if (form.is_valid() and form2.is_valid()):
            form.save()
            form2.save()
        return redirect ('home')
    return render(request, 'landing/duelistaEditar.html',{'user':user_logged, 'user2':usuario, 'form': form, 'form2': form2, 'rol': rol })


def verGrupos(request):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    duelista=Duelista.objects.get(usuario = usuario)
    print(duelista)
    grupo=Grupo.objects.filter(duelistas = duelista)
    return render(request, 'landing/grupos_duelistas.html',{'duelista':duelista, 'grupo':grupo, 'user2':usuario, 'user':user_logged,  'rol': rol})

def salirseDelGrupo(request,id):
    grupo_al_salir = Grupo.objects.get(group_id = id)
    user_logged=request.user
    usuario=Usuario.objects.get(usuario = user_logged)
    duelista=Duelista.objects.get(usuario = usuario)
    grupo_al_salir.duelistas.remove(duelista)
    grupo_al_salir.save()
    return redirect ('verGrupos')

def editarGrupo(request,id):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    grupo= Grupo.objects.get(group_id = id)
    user_avatar = usuario.avatar
    if request.method == 'POST':
        form = GrupoForm(request.POST,request.FILES,instance=grupo)
        if form.is_valid():
            form.save()
        return redirect ('verGrupos')
    else:
        form = GrupoForm(instance=grupo)
        return render(request,'landing/GrupoEditar.html',{'user':user_logged, 'user2':usuario, 'form': form, 'rol': rol , 'avatar': user_avatar})

def crearGrupo(request):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    duelista=Duelista.objects.get(usuario = usuario)
    user_avatar = usuario.avatar
    if request.method == 'POST':
        form = GrupoForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            grupoCreado = Grupo.objects.all().latest('group_id')
            grupoCreado.duelistas.add(duelista)
        return redirect ('verGrupos')
    else:
        form = GrupoForm()
        return render(request,'landing/GrupoCrear.html',{'user':user_logged, 'user2':usuario, 'form': form, 'rol': rol , 'avatar': user_avatar})

def eliminarGrupo(request,id):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    duelista=Duelista.objects.get(usuario = usuario)
    user_avatar = static(usuario.avatar)
    grupo = Grupo.objects.get(group_id = id)
    grupo.delete()
    return redirect ('verGrupos')


def verFichas(request):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    duelista=Duelista.objects.get(usuario = usuario)
    print(duelista)
    fichas=Ficha_Individual.objects.filter(duelista = duelista)
    return render(request, 'landing/fichas_registro.html',{'duelista':duelista, 'fichas':fichas, 'user2':usuario, 'user':user_logged,  'rol': rol})

def editarFicha(request,id):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    ficha= Ficha_Individual.objects.get(id_ficha = id)
    user_avatar = usuario.avatar
    if request.method == 'POST':
        form = FichaIndividualForm(request.POST,instance=ficha)
        if form.is_valid():
            form.save()
        return redirect ('verFichas')
    else:
        form = FichaIndividualForm(instance=ficha)
        return render(request,'landing/FichaEditar.html',{'user':user_logged, 'user2':usuario, 'form': form, 'rol': rol , 'avatar': user_avatar})

def eliminarFicha(request,id):
    user_logged=request.user
    rol = request.session['rol']
    usuario=Usuario.objects.get(usuario = user_logged)
    duelista=Duelista.objects.get(usuario = usuario)
    user_avatar = static(usuario.avatar)
    ficha= Ficha_Individual.objects.get(id_ficha = id)
    torneo = ficha.torneo
    print(torneo)
    torneo.numero_participantes_disponibles +=1
    torneo.save()
    ficha.delete()
    return redirect ('verFichas')

def verUsuariosIntoTheVrains(request):
    duelistas = Duelista.objects.all()
    return render(request,'landing/revisarDuelistas.html',{'duelistas': duelistas})

def estadistica(request,id):
    return render(request,'landing/estadistica.html')
