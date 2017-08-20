from django import forms
from apps.torneo.models import Torneo_Individual

class TorneoIndividualForm (forms.ModelForm):

    class Meta:
        model = Torneo_Individual

        fields = [
            'nombre',
            'fecha_hora_inicio',
            'fecha_hora_fin',
            'numero_participantes_disponibles',
            ]
        
