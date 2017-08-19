# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from apps.carta.forms import CartaForm
from apps.carta.models import Carta

# Create your views here.

def crearCarta(request):
    if request.method == 'POST':
        form = CartaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Producto agregado exitosamente!')
        return render(request,'landing/productos.html',{})
    else:
        form = CartaForm()
        return render(request,'landing/AgregarProducto.html',{'form': form})
