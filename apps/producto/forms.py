from django import forms
from apps.producto.models import Producto

class ProductForm (forms.ModelForm):

    class Meta:
        model = Producto

        fields = [
            'codigo',
            'nombre',
            'tipo',
            'fecha_salida',
            'url',
            ]
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'fecha_salida': 'Fecha Salida',
            'url': 'Url Imagen',
            }
