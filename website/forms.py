from django import forms
from .models import Proyecto

# Construcción o definición de los formularios
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'titulo',
            'descripcion',
            'categoria',
            'tecnologias',
            'etiquetas'
        ]