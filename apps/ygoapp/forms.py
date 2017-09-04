from django import forms
from apps.ygoapp.models import Usuario 
from django.contrib.auth.models import User

class UsuarioForm (forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'avatar',
            ]

        labels = {
            'avatar': 'Avatar',
            }
        widgets = {'avatar': forms.FileInput(attrs={'class':'form-control', 'name': 'avatar' })
        }
            
        

class UserForm (forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'password': 'Contrasenia',
        }  

        widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Nombre:'}),    
        'last_name':forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Apellido: '}),
        'email': forms.EmailInput(attrs={'class': 'form-control input-md', 'placeholder': 'Email: '}),
        'password':forms.PasswordInput(attrs={'class': 'form-control input-md', 'placeholder': 'Email: '})
        }