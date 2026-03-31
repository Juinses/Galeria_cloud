from django import forms
from .models import Imagen

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['titulo', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Título de la imagen'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
        }