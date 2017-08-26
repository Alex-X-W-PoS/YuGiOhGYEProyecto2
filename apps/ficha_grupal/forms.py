from django import forms
from apps.ficha_grupal.models import Ficha_Grupal
from apps.grupo.models import Grupo
from apps.jugador.models import Duelista

class SeleccionarGrupoForm (forms.ModelForm):
    def __init__(self,user,*args,**kwargs):
        super(SeleccionarGrupoForm,self).__init__(*args,**kwargs)
        self.fields['grupo'] = forms.ModelChoiceField(queryset=Grupo.objects.filter(duelistas=user))

    class Meta:
        model = Ficha_Grupal

        fields = [
            'torneo',
            'grupo',
            ]
        labels = {
            'torneo': 'Torneo',
            'grupo': 'Grupo',
            }
        widgets = {
            'torneo': forms.HiddenInput(),
            }

class FichaGrupalForm (forms.ModelForm):
    def __init__(self,grupo_select,*args,**kwargs):
        super(FichaGrupalForm,self).__init__(*args,**kwargs)
        self.fields['jugador1'] = forms.ModelChoiceField(queryset=Duelista.objects.filter(grupo=grupo_select))
        self.fields['jugador2'] = forms.ModelChoiceField(queryset=Duelista.objects.filter(grupo=grupo_select))
        self.fields['jugador3'] = forms.ModelChoiceField(queryset=Duelista.objects.filter(grupo=grupo_select))
        
    class Meta:
        model = Ficha_Grupal
        fields = [
            'torneo',
            'grupo',
            'jugador1',
            'deck1',
            'jugador2',
            'deck2',
            'jugador3',
            'deck3',
            ]
        labels = {
            'torneo': 'Torneo',
            'grupo': 'Grupo',
            'jugador1': 'Primer Jugador',
            'deck1': 'Deck',
            'jugador2': 'Segundo Jugador',
            'deck2': 'Deck',
            'jugador3': 'Tercer Jugador',
            'deck3': 'Deck',
            }
        widgets = {
            'torneo': forms.HiddenInput(),
            'grupo': forms.HiddenInput(),
            }
