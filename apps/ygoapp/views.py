# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from apps.ygoapp.forms import UsuarioForm, UserForm
from apps.ygoapp.models import Usuario
from apps.jugador.models import Duelista
from apps.grupo.models import Grupo
from django.contrib.auth.models import User
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
    user=Usuario.objects.get(user_id=4)
    

    ide=user.usuario_id
    usuario2=User.objects.get(id=ide)
    return render(request, 'landing/duelistaPerfil.html',{'user':usuario2, 'user2':user})


def editarPerfil(request):
    user=Usuario.objects.get(user_id=4)
    print(user.usuario.first_name)
    ide=user.usuario_id
    usuario2=User.objects.get(id=ide)
    if request.method=='GET':
        form= UsuarioForm(instance=user)
        form2= UserForm(instance=usuario2)
        #print(form)
    else:
        form=UsuarioForm(request.POST, instance=user)
        form2=UserForm(request.POST, instance=usuario2)
        #print(form)
        print(form2)
        if (form.is_valid() and form2.is_valid()):
            form.save()
            form2.save()
        return redirect ('home')
    return render(request, 'landing/duelistaEditar.html',{'user':usuario2, 'user2':user, 'form': form, 'form2': form2})


def verGrupos(request):
    user=Usuario.objects.get(user_id=4)
    usuario2=User.objects.get(id=user.usuario_id)
    duelista=Duelista.objects.get(id=user.usuario_id)
    print(duelista)
    duelista=Duelista.objects.all()
    grupo=Grupo.objects.all()
    for d in duelista:
        print("duelista",d.id)
    for g in grupo:       
        print("grupo",g.group_id) 
    return render(request, 'landing/grupos_duelistas.html',{'duelista':duelista, 'grupo':grupo, 'user2':user, 'user':usuario2})