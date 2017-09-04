# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from apps.grupo.models import Grupo
from django.db import connection
from collections import namedtuple
# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def convertir(self,querys):
	query = querys
	with connection.cursor() as cursor:
		cursor.execute(query,[self])
		con =  namedtuplefetchall(cursor)
		cursor.close()
	return con

def grupo(request):
	grupo = Grupo.objects.all().order_by('nombre')
	return render(request, 'landing/grupos.html' ,{"grupo":grupo})

def grupoEliminar(request,id):
	grupo1 = Grupo.objects.filter(group_id=id)
	if request.method == "POST":
		grupo1.delete()
		return redirect("grupos")
	return redirect("grupos")

def verLista(request,id):
	grupo1 = Grupo.objects.filter(group_id=id)
	liss = convertir(id,"select j.usuario_id ,u.rol,us.username from yugiohgye.usuario u,yugiohgye.jugador j,auth_user us,yugiohgye.grupo_duelistas gd where j.usuario_id = u.user_id and us.id = u.usuario_id and gd.duelista_id = j.id and gd.grupo_id = %s order by us.username asc")
	return render(request,'landing/gruposVerLista.html',{"grupo":grupo1,"lista":liss })


def crearGrupo(request):
	return render(request, 'landing/crear_grupo.html' ,{})