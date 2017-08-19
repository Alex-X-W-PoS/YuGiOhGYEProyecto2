from django import forms
from apps.carta.models import Carta

class CartaForm (forms.ModelForm):

    class Meta:
        model = Carta

        fields = [
            'codigo',
            'url',
            'producto',
            ]
        labels = {
            'codigo': 'Codigo',
            'url': 'Url Imagen',
            'producto': 'Producto'
            }
