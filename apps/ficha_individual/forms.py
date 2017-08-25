from django import forms
from apps.ficha_individual.models import Ficha_Individual

class FichaIndividualForm (forms.ModelForm):

    class Meta:
        model = Ficha_Individual

        fields = [
            'torneo',
            'duelista',
            'deck',
            ]
        labels = {
            'torneo': 'Torneo',
            'duelista': 'Duelista',
            'deck': 'Deck',
            }
        widgets = {
            'torneo': forms.HiddenInput(),
            'duelista': forms.HiddenInput(),
            }
