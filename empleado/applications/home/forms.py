from logging import PlaceHolder
from django import forms
from .models import Prueba



class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            "titulo",
            "subtitulo",
            "cantidad",
            )

        widgets = {
            "titulo": forms.TextInput (attrs= { "PlaceHolder": "ingrese texto aqui--"})
        }

    # validacion de datos en el form, antes de enviar datos
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 10:
            raise forms.ValidationError("Ingrese un numero mayor a 10")
        return cantidad