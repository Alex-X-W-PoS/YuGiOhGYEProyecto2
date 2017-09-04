from django import forms
from apps.grupo.models import Grupo

class CrearGrupoForm(models.Model):
	class Meta:
		model = Grupo
		
		fields = ['nombre','imagen']