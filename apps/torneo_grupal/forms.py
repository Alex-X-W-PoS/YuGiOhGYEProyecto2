from django import forms
from apps.torneo_grupal.models import Torneo_Grupal

class TorneoGrupalForm (forms.ModelForm):

    class Meta:
        model = Torneo_Grupal

        fields = [
            'nombre',
            'fecha_hora_inicio',
            'fecha_hora_fin',
            'numero_participantes_disponibles',
            ]
        
