# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from apps.ygoapp.forms import UsuarioForm

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
