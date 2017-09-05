# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from apps.comentario.models import Tema, Comentario
from apps.ygoapp.models import Usuario
from apps.comentario.forms import ComentarioForm

# Create your views here.

def verTemas(request):
    temas = Tema.objects.all()
    return render(request, 'landing/foro.html',{'temas':temas})

def verComentarios(request,id):
    context= {}
    tema = Tema.objects.get(id = id)
    context['tema'] = tema
    comentarios = Comentario.objects.filter(tema = tema)
    context['comentarios'] = comentarios
    user_logged = request.user
    usuario_log = Usuario.objects.get(usuario = user_logged)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verComentarios', id=id)
    else:
        data = {'usuario': usuario_log, 'tema': tema}
        form = ComentarioForm (initial=data)
        context['form']=form
        return render(request, 'landing/comentarios.html',context)
