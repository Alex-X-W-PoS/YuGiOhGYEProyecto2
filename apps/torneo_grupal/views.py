from django.shortcuts import render
from apps.torneo_grupal.models import Torneo_Grupal
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def listarTorneosGrupales(request):
    print('Aqui estamos')
    if request.is_ajax():
        data = Torneo_Grupal.objects.all().order_by('-fecha_hora_fin')
        response = serializers.serialize("json", data)
        return HttpResponse(response, content_type='application/json')
