from django import forms

class ContactoForm (forms.Form):
    OPCIONES =(('Queja', 'Queja'),
            ('Sugerencia', 'Sugerencia'),
            ('Pregunta de Productos', 'Pregunta de Productos'),
            ('Otros', 'Otros'))

    Motivo = forms.ChoiceField(choices=OPCIONES)
    Descripcion = forms.CharField(widget=forms.Textarea)
