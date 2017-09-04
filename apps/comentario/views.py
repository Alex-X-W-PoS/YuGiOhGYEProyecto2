# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from apps.comentario.forms import TemaForm,ComentarioForm
from apps.ygoapp.models import Usuario
from apps.comentario.models import Tema,Comentario
from django.contrib.auth.models import User
from django.db import connection
from collections import namedtuple
#from apps.auth_user.models import auth_user

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]



def foro(request):

	with connection.cursor() as cursor:
		cursor.execute('select t.id ,t.titulo,t.fecha, t.usuario_id,u.username,t.comentario from (select t.id ,t.titulo, t.fecha , t.usuario_id,count(c.id) as comentario  from  yugiohgye.tema t left join yugiohgye.comentario c on t.id=c.tema_id group by t.id ) t , yugiohgye.auth_user u ,yugiohgye.usuario us where u.id=us.usuario_id and t.usuario_id = us.user_id ')
		rows =  namedtuplefetchall(cursor)
		cursor.close()
	return render(request, 'landing/foro.html',{"lista":rows})

def crear_tema(request):
	cont = Usuario.objects.get(user_id=5)#ojo aqui se supone va el id del usuario
	ids = cont.usuario_id
	user = User.objects.get(id=ids)
	if request.method == "POST":
		data={
			'usuario':cont.user_id,
            'titulo':request.POST['titulo'],
            'descripcion':request.POST['descripcion']
		}
		form = TemaForm(data)
		if form.is_valid():
			form.save()
		return redirect('foro')
	else:
		return render(request, 'landing/tema_crear.html',{'datos':cont,'inforP':user})

def convertir(self):
	query = "select c.id,c.contenido,c.fecha,c.hora,c.tema_id, u.avatar, us.username FROM yugiohgye.comentario c ,yugiohgye.usuario u ,yugiohgye.auth_user us where c.usuario_id = u.user_id and u.usuario_id = us.id and c.tema_id = %s order by c.fecha"
	with connection.cursor() as cursor:
		cursor.execute(query,[self])
		comentario =  namedtuplefetchall(cursor)
		cursor.close()
	return comentario

def tema(request, id):
	tem = Tema.objects.get(id = id)
	usuario = Usuario.objects.get(user_id = tem.usuario_id)
	person = User.objects.get(id= usuario.usuario_id)
	if request.method == "POST":
		data = {
		    'usuario':request.POST['id_usuario'],
            'contenido':request.POST['contenido'],
            'tema':id
		}
		form1=ComentarioForm(data)
		if form1.is_valid():
			form1.save()
	comentario = convertir(id)
	return render(request, 'landing/temas.html',{"tema":tem ,"user":usuario,"person":person,"comentario":comentario})
	
