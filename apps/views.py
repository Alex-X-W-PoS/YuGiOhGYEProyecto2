from django.shortcuts import render
from apps.producto.models import Producto

def home(request):
    data = Producto.objects.all().order_by('-fecha_salida')[:4]
    return render(request,'landing/landing.html',{'data': data})

def timeline(request):
    return render(request,'landing/timeline.html',{})

def howToPlay(request):
    return render(request,'landing/comoSeJuega.html',{})

def estadisticas(request):
    return render(request,'landing/estadisticas.html',{})

def contactenos(request):
    return render(request,'landing/contactenos.html',{})
