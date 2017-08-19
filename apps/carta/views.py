# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from apps.carta.forms import CartaForm
from apps.carta.models import Carta
from apps.producto.models import Producto

# Create your views here.

def crearCarta(request):
    if request.method == 'POST':
        form = CartaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'landing/productos.html',{})
    else:
        form = CartaForm()
        return render(request,'landing/AgregarProducto.html',{'form': form})

def listaCartas(request):
        idi = request.GET['identificacion']
        context = {}
        cartas = Carta.objects.filter(producto__codigo = idi).order_by('codigo')
        context['cartas'] = cartas
        producto = Producto.objects.get(codigo= idi)
        context['producto'] = producto
        print('Aqui estamos')
        return render(request,'landing/galeriaCartas.html',context)
