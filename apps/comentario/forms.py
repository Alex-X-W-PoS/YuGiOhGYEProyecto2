from django import forms
from apps.comentario.models import Tema, Comentario

class ComentarioForm (forms.ModelForm):

    class Meta:
        model = Comentario

        fields = [
            'usuario',
            'contenido',
            'tema',
            ]
        widgets = {
            'usuario': forms.HiddenInput(),
            'tema': forms.HiddenInput(),
            }
