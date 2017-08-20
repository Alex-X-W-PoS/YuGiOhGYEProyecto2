from django import forms
from apps.ygoapp.models import Usuario

class UsuarioForm (forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'usuario',
            'rol',
            'avatar',
            'ranking',
            ]
        labels = {
            'usuario': 'Usuario',
            'rol': 'Rol',
            'avatar': 'Avatar',
            'ranking': 'Ranking'
            }
