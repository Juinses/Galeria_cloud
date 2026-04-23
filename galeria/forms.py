from django import forms
from .models import GaleriaFotos

class ImagenForm(forms.ModelForm):
    # Campo extra para subir el archivo (no está en la BD, es solo para el frontend)
    archivo = forms.ImageField(label="Seleccionar Imagen", required=False)

    class Meta:
        model = GaleriaFotos
        fields = ['foto', 'estado'] # Campos reales de la BD
        widgets = {
            'foto': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Nombre del archivo'}),
            'estado': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Estado (ej: Activo)'}),
        }