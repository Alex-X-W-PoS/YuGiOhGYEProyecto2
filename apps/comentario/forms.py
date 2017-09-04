from django import forms
from apps.comentario.models import Tema, Comentario

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema

        fields = [
            'usuario',
            'titulo',
            'descripcion',
            ]

class ComentarioForm(forms.ModelForm):
     class Meta:
        model = Comentario
        fields = [
             'usuario',
             'contenido',
             'tema',
            ]