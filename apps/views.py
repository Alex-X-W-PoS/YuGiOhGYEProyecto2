from django.shortcuts import render

def home(request):
    return render(request,'landing/landing.html',{})

def timeline(request):
    return render(request,'landing/timeline.html',{})

def howToPlay(request):
    return render(request,'landing/comoSeJuega.html',{})

def estadisticas(request):
    return render(request,'landing/estadisticas.html',{})

def contactenos(request):
    return render(request,'landing/contactenos.html',{})
