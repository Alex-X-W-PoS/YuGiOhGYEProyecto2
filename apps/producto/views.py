# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from apps.producto.forms import ProductForm
from django.contrib import messages
from apps.producto.models import Producto
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def productos(request):
    return render(request,'landing/productos.html',{})

def crearProducto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Producto agregado exitosamente!')
        return render(request,'landing/productos.html',{})
    else:
        form = ProductForm()
        return render(request,'landing/AgregarProducto.html',{'form': form})

def ajax_get_producto(request):
    print('Aqui estamos')
    if request.is_ajax():
        tipo_buscado = request.GET['tipo']
        data = Producto.objects.filter(tipo = tipo_buscado).order_by('-fecha_salida')
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')
        
