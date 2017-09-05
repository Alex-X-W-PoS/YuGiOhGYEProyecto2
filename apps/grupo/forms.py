from django import forms
from apps.grupo.models import Grupo
from apps.jugador.models import Duelista

class GrupoForm (forms.ModelForm):

    class Meta:
        model = Grupo

        fields = [
            'nombre',
            'imagen',
            ]
        
        labels = {
            'nombre': 'Nombre del Grupo',
            'imagen': 'Imagen del Grupo',
            }
        widgets = {
            'imagen': forms.FileInput(attrs={'class':'form-control', 'name': 'imagen' })
            }
            
class InvitingForm (forms.Form):
    Duelistas = forms.ModelMultipleChoiceField(queryset=Duelista.objects.all())
